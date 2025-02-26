import gpiozero
from scout import constants
import signal
import time

sensor = gpiozero.DistanceSensor(
    echo=constants.ULTRASONIC_PINS['echo'], trigger=constants.ULTRASONIC_PINS['trig'])


trigger = gpiozero.OutputDevice(constants.ULTRASONIC_PINS['trig'])
echo = gpiozero.InputDevice(constants.ULTRASONIC_PINS['echo'])


def get_distance():
    trigger.off()
    time.sleep(0.000002)
    trigger.on()
    time.sleep(0.000015)
    trigger.off()

    t3 = time.time()

    while not echo.is_active:
        t4 = time.time()
        if (t4 - t3) > 0.03:
            return -1

    t1 = time.time()
    while echo.is_active:
        t5 = time.time()
        if (t5 - t1) > 0.03:
            return -1

    t2 = time.time()
    time.sleep(0.01)
#    print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    return ((t2 - t1) * 340 / 2) * 100


if __name__ == '__main__':

    def signal_handler(sig, frame):
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print(get_distance())
        time.sleep(1)
