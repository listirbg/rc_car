# ######################
# Controller des RC-Cars
# ######################

# ### Modul-Imports
from machine import Pin, I2C, ADC, DAC
import sh1106
import pictures
import framebuf
import network
import espnow
import time


# Pin 12 für Boot auf Pull Down
Pin(12, Pin.IN, Pin.PULL_DOWN)


# ### Mac-Adressen
mac_controller = b'\x88\x13\xbfq\xc1\xcc'
mac_car = b'\xac\x15\x18\xe9\x98H'


# ### ESP-NOW initialisieren

# WLAN aktivieren
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(pm=sta.PM_NONE)

# ESP-NOW initialisieren
en = espnow.ESPNow()
en.active(True)

# Empfänger hinzufügen
en.add_peer(mac_car)


# ### Funktionen definieren

# Logo auf dem Display anzeigen
def show_logo(display: sh1106.SH1106, duration_s: int = 0) -> None:
    # Logo als Byte-Array
    logo = pictures.logo()

    # FrameBuffer für das Logo erstellen
    fb = framebuf.FrameBuffer(logo, 128, 64, framebuf.MONO_VLSB)

    # Logo auf dem Display anzeigen
    display.fill(0)
    display.blit(fb, 0, 0)
    display.show()
    time.sleep(duration_s)


# Analogen Eingang einlesen, Wert stabilisieren und in 0 .. +- 100 % umwandeln
def read_input_calc(analog_input: ADC, last_val: int, hysteresis: int, invert: bool = False) -> int:
    # Wert am ADC einlesen
    val = analog_input.read_u16()
    # Wert ggf. invertieren
    if invert:
        val = -(val - 65535)
    # In Wert 0-65 umwandeln
    val = val // 1000

    # Neuen Wert in +- 100 % berechnen
    new_val = int(((val / 64) * 200) - 100)

    # Wert stabilisieren
    if (32 - hysteresis) < val < (32 + hysteresis):
        send_val = 0
    elif (new_val - last_val) < -hysteresis or (new_val - last_val) > hysteresis: # Berechnung passt nicht
        send_val = new_val
    else:
        send_val = last_val

    send_val = max(-100, min(100, send_val))
    return send_val


# Sound abspielen
def play_sound(output: DAC, output_mute: Pin, sound: str, sample_rate: int = 8000, chunk_size: int = 2048) -> None:
    output_mute.value(1)
    # Zeit zwischen Samples berechnen
    delay = int((1 / sample_rate)*1_000_000)
    with open(sound, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            for sample in chunk:
                output.write(sample)
                time.sleep_us(delay)
    sound_mute.value(0)


# ### Ein-/Ausgänge definieren

# Display SH1106 OLED (I2C)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
oled = sh1106.SH1106_I2C(128, 64, i2c, rotate=180)

# Steuerung
# Joystick Gas
joystick_throttle = ADC(34)
joystick_throttle_button = Pin(19, Pin.IN, Pin.PULL_UP)
joystick_angle = ADC(35)
joystick_angle_button = Pin(18, Pin.IN, Pin.PULL_UP)

# Audio-Verstärker
sound_left_channel = DAC(25)  # nicht verwendet
sound_right_channel = DAC(26)
sound_mute = Pin(16, Pin.OUT)
sound_shutdown = Pin(17, Pin.OUT, value=1)

# Laderegler
charger_charging = Pin(14, Pin.IN, Pin.PULL_UP)
charger_standby = Pin(12, Pin.IN, Pin.PULL_UP)


# ### Programmablauf

# Logo im Display anzeigen
show_logo(oled, 0)

# Sound abspielen
play_sound(sound_right_channel, sound_mute, "startup.raw")

# Null-Werte definieren
send_val_throttle = 32
send_val_angle = 32


# ### Main-Loop
while True:
    # Werte einlesen
    send_val_throttle = read_input_calc(joystick_throttle, send_val_throttle, 2, True)
    send_val_angle = read_input_calc(joystick_angle, send_val_angle, 2, False)

    # Werte an RC-Car senden
    send_text = f"throttle:{send_val_throttle},angle:{send_val_angle}"
    en.send(mac_car, str(send_text), True)

    # Signalstärke überwachen
    en.recv()
    peers_table = en.peers_table
    # if peers_table[mac_car]:
    if mac_car in peers_table:
        #  0 .. 60: sehr gut, 61 .. 69: gut, 70 .. 78: ausreichend
        peer_signal_strength = -(peers_table[mac_car][0])
        if 0 <= peer_signal_strength <= 60:
            pic_signal = pictures.connection_3_16x16()
        elif 61 <= peer_signal_strength <= 69:
            pic_signal = pictures.connection_2_16x16()
        elif 70 <= peer_signal_strength <= 78:
            pic_signal = pictures.connection_1_16x16()
        else:
            pic_signal = pictures.connection_0_16x16()
    else:
        pic_signal = pictures.connection_0_16x16()

    # Anzeige Display
    oled.fill(0)

    # Fahrmodus max. Geschwindigkeit
    fb_tacho_max = framebuf.FrameBuffer(pictures.tacho_max_20x18(), 20, 18, framebuf.MONO_VLSB)
    oled.blit(fb_tacho_max, 1, 1)
    oled.text(f"100 %", 25, 8, 1)
    # oled.text(f"{max_throttle:3} %", 22, 1, 1)

    # Verbindung
    fb_connection = framebuf.FrameBuffer(pic_signal, 16, 16, framebuf.MONO_VLSB)
    oled.blit(fb_connection, 111, 1)

    # Aktuelle Geschwindigkeit
    fb_tacho = framebuf.FrameBuffer(pictures.tacho_30x30(), 30, 30, framebuf.MONO_VLSB)
    oled.blit(fb_tacho_max, 32, 32)
    oled.text(f"{send_val_throttle:4} %", 55, 38, 1)

    oled.show()
