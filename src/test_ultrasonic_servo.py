import gpiozero
from scout import constants
from scout.servo import Servo
import time
import signal

servo = Servo(constants.ULTRASONIC_PINS['servo'])

if __name__ == '__main__':

    def signal_handler(sig, frame):
        servo.close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for angle in [90, 135, 180, 135, 90, 45, 0, 45, 90]:
        servo.angle = angle
        time.sleep(1)
