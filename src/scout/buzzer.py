import gpiozero


class Buzzer(gpiozero.Buzzer):
    def __init__(self, pin):
        super().__init__(pin=pin, active_high=False)
