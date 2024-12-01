# ######################
# Controller des RC-Cars
# ######################


# ### Modul-Imports
from machine import Pin, I2C, ADC
from Software.Controller import sh1106, pictures
import framebuf
import network
import espnow
from time import sleep


# ### ESP-NOW initialisieren

# WLAN aktivieren
sta = network.WLAN(network.STA_IF)
sta.active(True)

# ESP-NOW initialisieren
en = espnow.ESPNow()
en.active(True)

# Empfänger hinzufügen
peer = b'\xac\x15\x18\xe9\x98H'
en.add_peer(peer)


# ### Funktionen definieren

# Logo auf dem Display anzeigen
def show_logo(display: sh1106.SH1106, duration_s: int = 3) -> None:
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
def read_input_calc(analog_input: ADC, last_val: int, hysteresis: int) -> int:
    # Wert am ADC einlesen und in Wert 0-65 umwandeln
    val = analog_input.read_u16() // 1000
    print(val)

    # Wert stabilisieren
    if (32-hysteresis) < val < (32+hysteresis):
        send_val = 0
    elif (val - last_val) < -hysteresis or (val - last_val) > hysteresis:
        send_val = int(((val / 64) * 200) - 100)
    else:
        send_val = 0

    return send_val


# ### Ein-/Ausgänge definieren

# Display SH1106 OLED (I2C)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
oled = sh1106.SH1106_I2C(128, 64, i2c, rotate=180)

# Joystick Gas
joystick_throttle = ADC(34)

#Joystick Lenkung
joystick_angle = ADC(33)


# ### Programmablauf

# Logo im Display anzeigen
show_logo(oled, 3)

# Null-Werte definieren
send_val_throttle = 32
send_val_angle = 32


# ### Main-Loop
while True:
    # Werte einlesen
    send_val_throttle = read_input_calc(joystick_throttle, send_val_throttle, 5)
    send_val_angle = read_input_calc(joystick_angle, send_val_angle, 5)

    # Werte an RC-Car senden
    en.send(peer, str(send_val_throttle), True)

    # Werte im Display anzeigen
    oled.fill(0)
    oled.text(f"{send_val_throttle} %", 10, 10, 1)
    oled.show()
