from scout.vehicle import Vehicle
from scout.camera import Camera
from scout.buzzer import Buzzer

import matplotlib.pyplot as plt
import numpy as np
import time
import signal
import cv2

vehicle = Vehicle()

def Capture_Line():
    vehicle.camera_system.camera.capture()
    img = vehicle.camera_system.camera.image_array

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray = cv2.bitwise_not(gray)
    edges = cv2.Canny(inverted_gray, 10, 50, apertureSize=3)
    
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=60,
        minLineLength=30,
        maxLineGap=10
    )    

    line_image = img.copy()
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.title("Edge Image")
    plt.imshow(edges, cmap="gray")
    plt.subplot(122)
    plt.title("Detected Lines via Hough Transform")
    plt.imshow(cv2.cvtColor(line_image, cv2.COLOR_BGR2RGB))
    plt.savefig("./capture.png")

if __name__ == '__main__':

    def close():
        vehicle.camera_system.pan_servo.close()
        vehicle.camera_system.tilt_servo.close()

    def signal_handler(sig, frame):
        close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    for angle in [90, 135, 180, 135, 90, 45, 0, 45, 90]:
        vehicle.camera_system.pan_servo.angle = angle
        time.sleep(1)

    for angle in [90, 135, 180, 135, 90, 45, 0, 45, 90]:
        vehicle.camera_system.tilt_servo.angle = angle
        time.sleep(1)
    # vehicle.camera_system.pan_servo.angle = 0
    Capture_Line()
    
    close()