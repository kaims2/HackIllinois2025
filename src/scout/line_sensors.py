import gpiozero
from scout import constants


class LineSensors:

    far_left_sensor: gpiozero.LineSensor
    middle_left_sensor: gpiozero.LineSensor
    middle_right_sensor: gpiozero.LineSensor
    far_right_sensor: gpiozero.LineSensor

    def __init__(self):
        self.far_left_sensor = gpiozero.LineSensor(
            constants.LINE_SENSOR_PINS['far_left'])
        self.middle_left_sensor = gpiozero.LineSensor(
            constants.LINE_SENSOR_PINS['middle_left'])
        self.middle_right_sensor = gpiozero.LineSensor(
            constants.LINE_SENSOR_PINS['middle_right'])
        self.far_right_sensor = gpiozero.LineSensor(
            constants.LINE_SENSOR_PINS['far_right'])
