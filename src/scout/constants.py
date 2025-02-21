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
        'enable': 16
    },
    'right_motor': {
        'input_1': 19,
        'input_2': 26,
        'enable': 13
    }
}


ULTRASONIC_PINS: types.UltrasonicPinsConfig = {
    'trig': 0,
    'echo': 1,
    'servo': 23
}

BUZZER_PIN: int = 8

INFRARED_PINS: types.InfraredPinsConfig = {
    'sensor_1': 3,
    'sensor_2': 5,
    'sensor_3': 4,
    'sensor_4': 18
}

CAMERA_PINS: types.CameraPinsConfig = {
    'pan_servo': 11,
    'tilt_servo': 8
}
