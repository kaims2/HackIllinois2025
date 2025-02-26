import gpiozero
from scout import constants
import time
import signal

pan_servo = gpiozero.AngularServo(
    constants.CAMERA_PINS['pan_servo'], min_angle=-90, max_angle=90)
tilt_servo = gpiozero.AngularServo(
    constants.CAMERA_PINS['tilt_servo'], min_angle=-135, max_angle=45)

if __name__ == '__main__':

    def close():
        pan_servo.close()
        tilt_servo.close()

    def signal_handler(sig, frame):
        close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for angle in [0, 45, 90, 45, 0, -45, -90, -45, 0]:
        pan_servo.angle = angle
        time.sleep(1)

    for angle in [0, 45, 0, -45, -90, -135, -90, -45, 0]:
        tilt_servo.angle = angle
        time.sleep(1)

    close()
