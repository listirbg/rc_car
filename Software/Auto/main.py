# #####################
# Steuerung des RC-Cars
# #####################


# ### Modul-Imports
from machine import Pin, PWM
import network
import espnow


# ### Initialisieren von ESP-Now

# WLAN aktivieren
sta = network.WLAN(network.STA_IF)
sta.active(True)

# ESP-NOW initialisieren
en = espnow.ESPNow()
en.active(True)


# ### Funktionen definieren

# Geschwindigkeit des Motors über den ESC steuern
def set_esc_motor_speed(output: PWM, speed: int) -> None:
    # Begrenze den Wert auf -100 bis 100
    speed = max(-100, min(100, speed))
    speed = speed * 0.2

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


# ### Ein-/Ausgänge definieren

# Motor (PWM Frequenz 50 Hz)
pin_motor = 12
pwm_motor = PWM(Pin(pin_motor), freq=50, duty_ns=1_500_000)

# Servo (PWM Frequenz 50 Hz)
pin_servo = 14
pwm_servo = PWM(Pin(pin_servo), freq=50, duty_ns=1_500_000)


# ### Main-Loop
while True:
    # Werte über ESP-Now empfangen
    host, msg = en.recv()
    print(msg)

    # Motor ansteuern
    motor_speed = int(msg)
    set_esc_motor_speed(pwm_motor, motor_speed)

    # Servo ansteuern
    servo_angle = int(msg)
    set_servo_angle(pwm_servo, 180, 70, 110, servo_angle)
