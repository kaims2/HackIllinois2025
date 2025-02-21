import typing


class LEDPinsConfig(typing.TypedDict):
    red: int
    green: int
    blue: int


class MotorPinsConfig(typing.TypedDict):
    input_1: int
    input_2: int
    enable: int


class DrivetrainPinsConfig(typing.TypedDict):
    left_motor: MotorPinsConfig
    right_motor: MotorPinsConfig


class UltrasonicPinsConfig(typing.TypedDict):
    trig: int
    echo: int
    servo: int


class InfraredPinsConfig(typing.TypedDict):
    sensor_1: int
    sensor_2: int
    sensor_3: int
    sensor_4: int


class CameraPinsConfig(typing.TypedDict):
    pan_servo: int
    tilt_servo: int
