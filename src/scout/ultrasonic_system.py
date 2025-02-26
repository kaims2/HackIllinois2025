import gpiozero
from scout import constants
from scout.servo import Servo


class UltrasonicSystem:

    ultrasonic: gpiozero.DistanceSensor
    leds: gpiozero.RGBLED
    servo: Servo

    def __init__(self):
        self.ultrasonic = gpiozero.DistanceSensor(
            echo=constants.ULTRASONIC_PINS['echo'], trigger=constants.ULTRASONIC_PINS['trig'])
        self.leds = gpiozero.RGBLED(
            red=constants.LED_PINS['red'], green=constants.LED_PINS['green'], blue=constants.LED_PINS['blue'])
        self.servo = Servo(constants.ULTRASONIC_PINS['servo'])
