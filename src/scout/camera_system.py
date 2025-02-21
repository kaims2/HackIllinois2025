import gpiozero
from scout import constants


class CameraSystem:

    pan_servo: gpiozero.Servo
    tilt_servo: gpiozero.Servo

    def __init__(self):

        self.pan_servo = gpiozero.Servo(constants.CAMERA_PINS['pan_servo'])
        self.tilt_servo = gpiozero.Servo(constants.CAMERA_PINS['tilt_servo'])
