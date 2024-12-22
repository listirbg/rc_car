# #####################
# Steuerung des RC-Cars
# #####################


# ### Modul-Imports
from machine import Pin, PWM
import network
import espnow
from time import sleep


# ### Mac-Adressen
mac_controller = b'\x88\x13\xbfq\xc1\xcc'
mac_car = b'\xa0\xb7e-\xc4\xc4'


# ### Initialisieren von ESP-Now

# WLAN aktivieren
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(pm=sta.PM_NONE)

# ESP-NOW initialisieren
en = espnow.ESPNow()
en.active(True)

# Empfänger hinzufügen
en.add_peer(mac_controller)


# ### Funktionen definieren

# Geschwindigkeit des Motors über den ESC steuern
def set_esc_motor_speed(output: PWM, speed: int) -> None:
    # Begrenze den Wert auf -100 bis 100
    speed = max(-100, min(100, speed))

    # Ansteuerung Motor
    # Periodendauer 20 ms (= 50 Hz)
    # 1,0 ms = -100 %; 1,5 ms = 0 %; 2,0 ms = +100 %
    pwm_speed_ns = int((speed / 100) * 500_000 + 1_500_000)
    output.duty_ns(pwm_speed_ns)


# Winkel des Servomotors steuern
def set_servo_angle(output: PWM, possible_angle: int, min_angle: int, max_angle: int, angle_percent: int) -> None:
    # Begrenze den Wert auf -100 bis 100
    angle_percent = max(-100, min(100, angle_percent))

    # Faktor für max. Winkel berechnen
    factor = 0
    if angle_percent < 0:
        extreme_angle = min_angle
        factor = ((possible_angle / 2 - extreme_angle) / 90) * 1_000_000
    elif angle_percent > 0:
        extreme_angle = max_angle
        factor = (-(possible_angle / 2 - extreme_angle) / 90) * 1_000_000

    # Ansteuerung Servo
    # Periodendauer 20 ms (= 50 Hz)
    # 0,5 ms = -100 %; 1,5 ms = 0 %; 2,5 ms = +100 %
    pwm_speed_ns = int((angle_percent / 100) * factor + 1_500_000)
    output.duty_ns(pwm_speed_ns)


# Empfangene Nachricht in Dict umwandeln
def convert_msg(message: str) -> dict[str, int]:
    message = str(message)
    # Einzelne Werte aufteilen
    message_table = message.split(",")

    message_dict = dict()

    # Werte in Bezeichnung und Wert aufteilen
    for obj in message_table:
        part = obj.split(":")
        key = part[0].strip("b'")
        value = int(part[1].strip("'"))
        message_dict[key] = value

    return message_dict


# ### Ein-/Ausgänge definieren

# Motor (PWM Frequenz 50 Hz)
pin_motor = 12
motor = Pin(pin_motor, Pin.OUT, value=0)
sleep(1)
pwm_motor = PWM(Pin(pin_motor), freq=50, duty_ns=1_500_000)

# Servo (PWM Frequenz 50 Hz)
pin_servo = 14
pwm_servo = PWM(Pin(pin_servo), freq=50, duty_ns=1_500_000)


# ### Main-Loop
while True:
    # Nachricht zum Ermitteln der Verbindungsstärke
    en.send(mac_controller, "SYN")
    # Alten Wert aus Variable msg löschen
    msg = None

    # Werte über ESP-Now empfangen
    host, msg = en.recv()

    # Motorgeschwindigkeit und Lenkwinkel festlegen
    values_dict = convert_msg(msg)
    motor_speed = values_dict['throttle']
    servo_angle = values_dict['angle']

    # Motor und Servo ansteuern
    set_esc_motor_speed(pwm_motor, motor_speed)
    set_servo_angle(pwm_servo, 180, 70, 110, servo_angle)
