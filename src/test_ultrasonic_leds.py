import gpiozero
from scout import constants
import time
import signal


led = gpiozero.RGBLED(
    constants.LED_PINS['red'], constants.LED_PINS['green'], constants.LED_PINS['blue'])


if __name__ == '__main__':

    def signal_handler(sig, frame):
        led.off()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    led.color = (1, 0, 0)
    time.sleep(1)
    led.color = (0, 1, 0)
    time.sleep(1)
    led.color = (0, 0, 1)
    time.sleep(1)
    led.color = (1, 1, 0)
    time.sleep(1)
    led.color = (0, 1, 1)
    time.sleep(1)
    led.color = (1, 0, 1)
    time.sleep(1)
    led.color = (1, 1, 1)
    time.sleep(1)
    led.off()
