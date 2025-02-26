import gpiozero
from scout import constants


class UltrasonicSystem:

    ultrasonic: gpiozero.DistanceSensor
    leds: gpiozero.RGBLED
    servo: gpiozero.AngularServo

    def __init__(self):
        self.ultrasonic = gpiozero.DistanceSensor(
            echo=constants.ULTRASONIC_PINS['echo'], trigger=constants.ULTRASONIC_PINS['trig'])
        self.leds = gpiozero.RGBLED(
            red=constants.LED_PINS['red'], green=constants.LED_PINS['green'], blue=constants.LED_PINS['blue'])
        self.servo = gpiozero.AngularServo(
            pin=constants.ULTRASONIC_PINS['servo'], max_angle=90, min_angle=-90)
