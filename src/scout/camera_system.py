import gpiozero
from scout import constants
from scout.camera import Camera
from scout.servo import Servo


class CameraSystem:

    pan_servo: Servo
    tilt_servo: Servo
    camera: Camera

    def __init__(self):
        self.pan_servo = Servo(constants.CAMERA_PINS['pan_servo'])
        self.tilt_servo = Servo(constants.CAMERA_PINS['tilt_servo'])
        self.camera = Camera()
