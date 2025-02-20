import gpiozero
from scout import constants
import time
import signal


red_led = gpiozero.LED(constants.LED_PINS['red'])
green_led = gpiozero.LED(constants.LED_PINS['green'])
blue_led = gpiozero.LED(constants.LED_PINS['blue'])

if __name__ == '__main__':

    def signal_handler(sig, frame):
        red_led.off()
        green_led.off()
        blue_led.off()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    red_led.on()
    time.sleep(1)
    red_led.off()
    green_led.on()
    time.sleep(1)
    green_led.off()
    blue_led.on()
    time.sleep(1)
    blue_led.off()
