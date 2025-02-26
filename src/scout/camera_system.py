import gpiozero
from scout import constants
from scout.camera import Camera


class CameraSystem:

    pan_servo: gpiozero.AngularServo
    tilt_servo: gpiozero.AngularServo
    camera: Camera

    def __init__(self):

        self.pan_servo = gpiozero.AngularServo(
            pin=constants.CAMERA_PINS['pan_servo'], max_angle=90, min_angle=-90)
        self.tilt_servo = gpiozero.AngularServo(
            constants.CAMERA_PINS['tilt_servo'], max_angle=45, min_angle=-135)
        self.camera = Camera()
