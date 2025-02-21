import gpiozero
from scout import constants
import time
import signal

pan_servo = gpiozero.Servo(constants.CAMERA_PINS['pan_servo'])
tilt_servo = gpiozero.Servo(constants.CAMERA_PINS['tilt_servo'])

if __name__ == '__main__':

    def close():
        pan_servo.close()
        tilt_servo.close()

    def signal_handler(sig, frame):
        close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    pan_servo.min()
    tilt_servo.min()
    time.sleep(1)
    pan_servo.mid()
    tilt_servo.mid()
    time.sleep(1)
    pan_servo.max()
    tilt_servo.max()
    time.sleep(1)
    pan_servo.mid()
    tilt_servo.mid()

    close()
