import gpiozero
from scout import constants


class Drivetrain:
    left_motor: gpiozero.Motor
    right_motor: gpiozero.Motor

    def __init__(self):
        self.left_motor = gpiozero.Motor(
            forward=constants.DRIVETRAIN_PIN['left_motor']['forward'],
            backward=constants.DRIVETRAIN_PIN['left_motor']['backward'],
            pwm=constants.DRIVETRAIN_PIN['left_motor']['enable  '],
        )

        self.right_motor = gpiozero.Motor(
            forward=constants.DRIVETRAIN_PIN['right_motor']['input_1'],
            backward=constants.DRIVETRAIN_PIN['right_motor']['input_2'],
            pwm=constants.DRIVETRAIN_PIN['right_motor']['enable'],
        )
