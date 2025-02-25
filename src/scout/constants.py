from scout import types

LED_PINS: types.LEDPinsConfig = {
    'red': 22,
    'green': 27,
    'blue': 24
}


DRIVETRAIN_PIN: types.DrivetrainPinsConfig = {
    'left_motor': {
        'input_1': 20,
        'input_2': 21,
        'enable': 12  # original wiring is 16
    },
    'right_motor': {
        'input_1': 16,  # original is 19,
        'input_2': 26,
        'enable': 13
    }
}


ULTRASONIC_PINS: types.UltrasonicPinsConfig = {
    'trig': 5,  # 0,
    'echo': 6,  # 1,
    'servo': 23,  # 23
}

BUZZER_PIN: int = 8

LINE_SENSOR_PINS: types.LineSensorPinsConfig = {
    'far_left':  25,  # 3
    'middle_left': 17,  # 5
    'middle_right': 4,  # 4
    'far_right': 18,  # 18
}

CAMERA_PINS: types.CameraPinsConfig = {
    'pan_servo': 19,  # 9
    'tilt_servo': 11  # 11
}
