import gpiozero
from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory
Device.pin_factory = PiGPIOFactory()

from scout.vehicle import Vehicle

import matplotlib.pyplot as plt
import numpy as np
import time
import signal
import cv2

vehicle = Vehicle()


v_num = 1

if __name__ == '__main__':

    def close():
        vehicle.camera_system.pan_servo.close()
        vehicle.camera_system.tilt_servo.close()

    def signal_handler(sig, frame):
        close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    
    
    vehicle.camera_system.tilt_servo.angle = 90
    vehicle.camera_system.pan_servo.angle = 90
    vehicle.camera_system.camera.capture()

    img = vehicle.camera_system.camera.image_array
    plt.figure(dpi=200)
    plt.imshow(img)
    plt.savefig("./violation_"+str(v_num)+".png")

    

    time.sleep(1)
    # vehicle.camera_system.pan_servo.angle = 0 