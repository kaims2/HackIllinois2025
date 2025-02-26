import gpiozero


class Servo(gpiozero.AngularServo):
    def __init__(self, pin):
        super().__init__(pin=pin, max_angle=180, min_angle=0,
                         min_pulse_width=0.0005, max_pulse_width=0.0025, initial_angle=90)
