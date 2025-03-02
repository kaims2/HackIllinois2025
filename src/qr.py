import cv2
from pyzbar import pyzbar
import gpiozero
from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory
Device.pin_factory = PiGPIOFactory()
from scout import constants
from scout.servo import Servo
from scout.drivetrain import Drivetrain
from scout.line_sensors import LineSensors
from scout.camera import Camera
from scout.buzzer import Buzzer
import time
import numpy as np
import matplotlib.pyplot as plt
import signal

camera = Camera()

pan_servo = Servo(constants.CAMERA_PINS['pan_servo'])
tilt_servo = Servo(constants.CAMERA_PINS['tilt_servo'])


def initialize():
    
    pan_servo.angle = 180
    tilt_servo.angle = 90

    while True:
        camera.capture()
        img = camera.image_array
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        qr_code = pyzbar.decode(gray)

        plt.figure()
        plt.imshow(gray, cmap="gray")
        plt.savefig("./capture.png")
        data = qr_code.data.decode("utf-8")
        print(data)
        time.sleep(1)
        if qr_code:
            data = qr_code[0].data.decode("utf-8")
            break
        else:
            data = None
        

if __name__ == '__main__':

    def close():
        pan_servo.close()
        tilt_servo.close()

    def signal_handler(sig, frame):
        close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)



    initialize()