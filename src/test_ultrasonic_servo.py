import gpiozero
from scout import constants
import time
import signal

servo = gpiozero.Servo(constants.ULTRASONIC_PINS['servo'])

if __name__ == '__main__':

    def signal_handler(sig, frame):
        servo.close()
        exit(0)

    servo.min()
    time.sleep(1)
    servo.mid()
    time.sleep(1)
    servo.max()
    time.sleep(1)
    servo.mid()
    servo.close()
