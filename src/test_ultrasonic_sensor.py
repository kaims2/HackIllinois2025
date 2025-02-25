import gpiozero
from scout import constants
import signal
import time

sensor = gpiozero.DistanceSensor(
    echo=constants.ULTRASONIC_PINS['echo'], trigger=constants.ULTRASONIC_PINS['trig'])

if __name__ == '__main__':

    def signal_handler(sig, frame):
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print(sensor.distance)
        time.sleep(1)
