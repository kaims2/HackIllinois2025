import gpiozero
from scout import constants
from scout.drivetrain import Drivetrain
import time

drivetrain = Drivetrain()


def test_motor(motor: gpiozero.Motor):
    for i in range(100):
        motor.forward(100)
        time.sleep(1/100)

    for i in range(99, -1, -1):
        motor.forward(i)
        time.sleep(1/99)

    for i in range(100):
        motor.backward(100)
        time.sleep(1/100)

    for i in range(99, -1, -1):
        motor.backward(i)
        time.sleep(1/99)

    motor.stop()


if __name__ == '__main__':

    print('testing left motor')
    test_motor(drivetrain.left_motor)

    print('testing right motor')
    test_motor(drivetrain.right_motor)
