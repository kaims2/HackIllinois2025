import gpiozero
from scout import constants
from scout.servo import Servo
import time
import signal

pan_servo = Servo(constants.CAMERA_PINS['pan_servo'])
tilt_servo = Servo(constants.CAMERA_PINS['tilt_servo'])

if __name__ == '__main__':

    def close():
        pan_servo.close()
        tilt_servo.close()

    def signal_handler(sig, frame):
        close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for angle in [90, 135, 180, 135, 90, 45, 0, 45, 90]:
        pan_servo.angle = angle
        time.sleep(1)

    for angle in [90, 135, 180, 135, 90, 45, 0, 45, 90]:
        tilt_servo.angle = angle
        time.sleep(1)

    close()
