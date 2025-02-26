import gpiozero
from scout import constants
import time
import signal

servo = gpiozero.AngularServo(
    constants.ULTRASONIC_PINS['servo'], max_angle=90, min_angle=-90)

if __name__ == '__main__':

    def signal_handler(sig, frame):
        servo.close()
        exit(0)

    for angle in [0, 45, 90, 45, 0, -45, -90, -45, 0]:
        servo.angle = angle
        time.sleep(1)
