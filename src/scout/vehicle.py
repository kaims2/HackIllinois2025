from scout.camera_system import CameraSystem
from scout.drivetrain import Drivetrain
from scout.line_sensors import LineSensors
from scout.ultrasonic_system import UltrasonicSystem
from scout.buzzer import Buzzer
from scout import constants


class Vehicle:

    camera_system: CameraSystem
    drivetrain: Drivetrain
    line_sensors: LineSensors
    ultrasonic_system: UltrasonicSystem
    buzzer: Buzzer

    def __init__(self):
        self.camera_system = CameraSystem()
        self.drivetrain = Drivetrain()
        self.line_sensors = LineSensors()
        self.ultrasonic_system = UltrasonicSystem()
        self.buzzer = Buzzer(constants.BUZZER_PIN)

    def run(self):
        pass
