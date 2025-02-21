import gpiozero
from scout import constants
from scout.drivetrain import Drivetrain
import time
import signal

drivetrain = Drivetrain()


def test_motor(motor: gpiozero.Motor):
    for i in range(100):
        motor.forward(i/100)
        time.sleep(1/100)

    for i in range(99, -1, -1):
        motor.forward(i/100)
        time.sleep(1/99)

    for i in range(100):
        motor.backward(i/100)
        time.sleep(1/100)

    for i in range(99, -1, -1):
        motor.backward(i/100)
        time.sleep(1/99)

    motor.stop()


if __name__ == '__main__':

    def signal_handler(sig, frame):
        drivetrain.left_motor.close()
        drivetrain.right_motor.close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    print('testing left motor')
    test_motor(drivetrain.left_motor)

    print('testing right motor')
    test_motor(drivetrain.right_motor)
