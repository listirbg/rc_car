# ######################
# Controller des RC-Cars
# ######################


# ### Modul-Imports
from machine import Pin, I2C, ADC, DAC
import sh1106
import pictures
import sounds
import framebuf
import network
import espnow
from time import sleep


# ### Mac-Adressen
mac_controller = b'\x88\x13\xbfq\xc1\xcc'
mac_car = b'\xac\x15\x18\xe9\x98H'


# ### ESP-NOW initialisieren

# WLAN aktivieren
sta = network.WLAN(network.STA_IF)
sta.active(True)

# ESP-NOW initialisieren
en = espnow.ESPNow()
en.active(True)
sta.config(pm=sta.PM_NONE)

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
    sleep(duration_s)


# Analogen Eingang einlesen, Wert stabilisieren und in 0 .. +- 100 % umwandeln
def read_input_calc(analog_input: ADC, last_val: int, hysteresis: int, invert: bool = False) -> int:
    # Wert am ADC einlesen
    val = analog_input.read_u16()
    # Wert ggf. invertieren
    if invert:
        val = -(val - 65535)
    # In Wert 0-65 umwandeln
    val = val // 1000

    # Wert stabilisieren
    if (32-hysteresis) < val < (32+hysteresis):
        send_val = 0
    elif (val - last_val) < -hysteresis or (val - last_val) > hysteresis:
        send_val = int(((val / 64) * 200) - 100)
    else:
        send_val = 0

    send_val = max(-100, min(100, send_val))
    return send_val


# Sound abspielen
def play_sound(output: DAC, sound: bytes, sample_rate: int = 8000) -> None:
    # Zeit zwischen Samples berechnen
    delay = 1 / sample_rate
    for sample in sound:
        # Schreibe den 8-bit-Wert in den DAC
        output.write(sample)
        sleep(delay)


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
sound_shutdown = Pin(17, Pin.OUT)

# Laderegler
charger_charging = Pin(14, Pin.IN, Pin.PULL_UP)
charger_standby = Pin(12, Pin.IN, Pin.PULL_UP)


# ### Programmablauf

# Logo im Display anzeigen
show_logo(oled, 0)

# Sound abspielen
play_sound(sound_right_channel, sounds.startup_sound())

# Null-Werte definieren
send_val_throttle = 32
send_val_angle = 32


# ### Main-Loop
while True:
    # Werte einlesen
    send_val_throttle = read_input_calc(joystick_throttle, send_val_throttle, 3, True)
    send_val_angle = read_input_calc(joystick_angle, send_val_angle, 3, False)

    # Werte an RC-Car senden
    send_text = f"throttle:{send_val_throttle},angle:{send_val_angle}"
    en.send(mac_car, str(send_text), True)

    # Signalstärke überwachen
    peers_table = en.peers_table
    # peer_signal_strength = 100 * (1 + ((peers_table[mac_car][0] + 30) / 97))

    # Werte im Display anzeigen
    oled.fill(0)
    oled.text(f"Geschwindigkeit:", 5, 5, 1)
    oled.text(f"{send_val_throttle} %", 5, 15, 1)
    oled.text(f"Lenkwinkel:", 5, 35, 1)
    oled.text(f"{send_val_angle} %", 5, 45, 1)
    # oled.text(f"Verbindung: {peer_signal_strength} %", 10, 30, 1)
    oled.show()
