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
from full_line import back_to_line_left, back_to_line_right
import time
import numpy as np
import matplotlib.pyplot as plt
import signal
# from qr import initialize
from pyzbar import pyzbar
import cv2

last_reset_time = 0
reset_interval = 5
object_idx = 1
human_idx = 1
drivetrain = Drivetrain()
line_sensors = LineSensors()
sensor = gpiozero.DistanceSensor(
    echo=constants.ULTRASONIC_PINS['echo'], trigger=constants.ULTRASONIC_PINS['trig'])
led = gpiozero.RGBLED(
    constants.LED_PINS['red'], constants.LED_PINS['green'], constants.LED_PINS['blue'])
buzzer = Buzzer(constants.BUZZER_PIN)
camera = Camera()
pan_servo = Servo(constants.CAMERA_PINS['pan_servo'])
tilt_servo = Servo(constants.CAMERA_PINS['tilt_servo'])
servo = Servo(constants.ULTRASONIC_PINS['servo'])

def move(left, right):
    if left >= 0:
        drivetrain.left_motor.forward(left)
    else:
        drivetrain.left_motor.backward(-left)
    if right >= 0:
        drivetrain.right_motor.forward(right)
    else:
        drivetrain.right_motor.backward(-right)

def reset():
    global last_reset_time
    current_time = time.time()
    if current_time - last_reset_time >= reset_interval:
        drivetrain.left_motor.stop()
        drivetrain.right_motor.stop()
        led.color = (1, 1, 1)
        time.sleep(0.25)
        led.off()
        led.color = (1, 0, 1)
        time.sleep(0.25)
        led.off()
        led.color = (0, 1, 1)
        time.sleep(0.25)
        led.off()
        led.color = (1, 1, 0)
        time.sleep(0.25)
        led.off()
        last_reset_time = current_time

def Check_Human(distance):
    move(0, 0)
    for i in range(4):
        buzzer.on()
        time.sleep(0.25)
        buzzer.off()
        time.sleep(0.25)
    d_end = sensor.distance
    if d_end > distance:
        return True
    return False

def led_show():
    led.color = (1, 0, 0)
    time.sleep(0.2)
    led.color = (0, 1, 0)
    time.sleep(0.2)
    led.color = (0, 0, 1)
    time.sleep(0.2)
    led.color = (1, 1, 0)
    time.sleep(0.2)
    led.color = (0, 1, 1)
    time.sleep(0.2)
    led.color = (1, 0, 1)
    time.sleep(0.2)
    led.color = (1, 1, 1)
    time.sleep(0.2)
    led.off()

def initialize():
    
    pan_servo.angle = 0
    tilt_servo.angle = 30

    print("Waiting for QR code")

    while True:
        camera.capture()
        img = camera.image_array
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        qr_code = pyzbar.decode(gray)
        print("Captured!")

        plt.figure()
        plt.imshow(gray, cmap="gray")
        plt.savefig("./capture.png")

        time.sleep(1)
        if qr_code:
            data = qr_code[0].data.decode("utf-8")
            print(data)
            time.sleep(3)
            led_show()
            break
        else:
            data = None
    print("Success")

    pan_servo.angle = 90
    time.sleep(0.5)
    

def Move_Around():
    global object_idx
    distances = []
    servo.angle = 25
    time.sleep(0.5)
    tilt_servo.angle = 0
    pan_servo.angle = 90
    time.sleep(0.5)
    camera.capture()
    img = camera.image_array
    fig = plt.figure()
    plt.imshow(img)
    plt.savefig(f"Object{object_idx}_Front.png")
    for angle in range(30, 150, 1):
        servo.angle = angle
        time.sleep(0.03)
        distance = sensor.distance
        distances.append(distance)
    fig = plt.figure()
    plt.plot(range(30, 150, 1), distances, 'o-')
    plt.savefig("Test.png")
    turn_left = 0 if np.arange(30,150)[np.argmax(distances)] < 90 else 1
    count = 0
    exit_loop = False
    if turn_left:
        move(-0.5, 0.5)
        servo.angle = 30
        time.sleep(0.6)
        move(0, 0)
        while True:
            for i in range(100):
                reset()
                move(0.4, 0.4)
                if i == 50 and count == 1:
                    move(0, 0)
                    tilt_servo.angle = 10
                    pan_servo.angle = 0
                    time.sleep(1)
                    camera.capture()
                    img = camera.image_array
                    fig = plt.figure()
                    plt.imshow(img)
                    plt.savefig(f"Object{object_idx}_Side.png")
                    move(0.4, 0.4)
                time.sleep(0.01)
                if not line_sensors.far_right_sensor.value and not line_sensors.middle_right_sensor.value:
                    exit_loop = True
                    break
            if exit_loop:
                break
            total = 60
            for i in range(total):
                reset()
                move(0.5, -0.5)
                time.sleep(0.01)
                if not line_sensors.far_left_sensor.value and not line_sensors.middle_right_sensor.value:
                    exit_loop = True
                    break
            if exit_loop:
                break
            count += 1
            if count > 5:
                break
        print(count, "Line Detected?")
        move(0, 0)
        servo.angle = 90
        led.color = (1, 0, 0)
        time.sleep(0.5)
        led.color = (0, 1, 0)
        time.sleep(0.5)
        led.color = (0, 0, 1)
        time.sleep(0.5)
        move(0.4, 0.4)
        time.sleep(0.15)
        while True:
            det1 = not line_sensors.far_left_sensor.value #left most
            det2 = not line_sensors.middle_left_sensor.value
            det3 = not line_sensors.middle_right_sensor.value
            det4 = not line_sensors.far_right_sensor.value #right most

            print(det1, det2, det3, det4)

            move(-0.5,0.5)
            time.sleep(0.05)
            if (det2 or det3)==True:
                break
    else:
        move(0.5, -0.5)
        servo.angle = 150
        time.sleep(0.7)
        move(0, 0)

        while True:
            for i in range(100):
                reset()
                move(0.4, 0.4)
                if i == 50 and count == 1:
                    move(0, 0)
                    tilt_servo.angle = 10
                    pan_servo.angle = 180
                    time.sleep(1)
                    camera.capture()
                    img = camera.image_array
                    fig = plt.figure()
                    plt.imshow(img)
                    plt.savefig(f"Object{object_idx}_Side.png")
                    move(0.4, 0.4)
                time.sleep(0.01)
                if not line_sensors.far_left_sensor.value and not line_sensors.middle_left_sensor.value:
                    exit_loop = True
                    break
            if exit_loop:
                break
            total = 60
            for i in range(total):
                reset()
                move(-0.5, 0.5)
                time.sleep(0.01)
                if not line_sensors.far_left_sensor.value and not line_sensors.middle_left_sensor.value:
                    exit_loop = True
                    break
            if exit_loop:
                break
            count += 1
            if count > 5:
                break
        print(count, "Line Detected?")
        move(0, 0)
        servo.angle = 90
        led.color = (1, 0, 0)
        time.sleep(0.5)
        led.color = (0, 1, 0)
        time.sleep(0.5)
        led.color = (0, 0, 1)
        time.sleep(0.5)
        move(0.4, 0.4)
        time.sleep(0.15)
        while True:
            det1 = not line_sensors.far_left_sensor.value #left most
            det2 = not line_sensors.middle_left_sensor.value
            det3 = not line_sensors.middle_right_sensor.value
            det4 = not line_sensors.far_right_sensor.value #right most

            move(0.5, -0.5)
            time.sleep(0.05)
            if (det2 or det3)==True:
                break
    move(0, 0)
    time.sleep(1)
    object_idx += 1
        
    # while True:
        # init_dist = sensor.distance
        # move(0.3, 0.3)
        # time.sleep(0.8)
        # move(0.4 * turn_left - 0.2 * ((turn_left + 1) % 2), 0.4 * ((turn_left + 1) % 2) - 0.2 * turn_left)
        # while sensor.distance >= init_dist - 0.08 :
        #     time.sleep(0.01)
        # move(0, 0)
        # move(0.4 * ((turn_left + 1) % 2) - 0.2 * turn_left, 0.4 * turn_left - 0.2 * ((turn_left + 1) % 2))
        # time.sleep(1.5)
        # move(0, 0)
    return


def trace():

    # f_speed, b_speed = 0.35, 0.55

    f_speed, b_speed = 0.4, 0.4

    while True:

        reset()
        distance = sensor.distance
        servo.angle = 90
        move(0.35, -0.35)
        
        det1 = not line_sensors.far_left_sensor.value #left most
        det2 = not line_sensors.middle_left_sensor.value
        det3 = not line_sensors.middle_right_sensor.value
        det4 = not line_sensors.far_right_sensor.value #right most

        print(det1, det2, det3, det4)

        # move(0.5 * det2 - 0.3 * det1, 0.5 * det3 - 0.3 * det4)
        # print(0.5 * det2 - 0.3 * det1, 0.5 * det3 - 0.3 * det4, '\n')

        # move(f_speed * det2 - b_speed * det1, f_speed * det3 - b_speed * det4)
        # print(f_speed * det2 - b_speed * det1, f_speed * det3 - b_speed * det4, '\n')
        move(f_speed * det2 + b_speed * det4, f_speed * det3 + b_speed * det1)
        print(f_speed * det2 + b_speed * det4, f_speed * det3 + b_speed * det1, '\n')

        if (f_speed * det2 - b_speed * det1 == 0) & (f_speed * det3 - b_speed * det4 == 0):
            move(-0.3, 0.3)

        if distance < 0.25:
            print("Obstable!")
            move(0, 0)
            human = Check_Human(distance)
            if human:
                global human_idx
                print("Human")
                tilt_servo.angle = 50
                pan_servo.angle = 90
                time.sleep(0.5)
                camera.capture()
                img = camera.image_array
                fig = plt.figure()
                plt.imshow(img)
                plt.savefig(f"Human{human_idx}_Front.png")
                time.sleep(2)
                human_idx += 1
            else:
                print("Object")
                Move_Around()
                time.sleep(1)

        time.sleep(0.1)

if __name__ == '__main__':
    initialize()

    last_reset_time = time.time()

    def signal_handler(sig, frame):
        try:
            buzzer.off()
            led.off()
            drivetrain.left_motor.close()
            drivetrain.right_motor.close()
            servo.close()
            pan_servo.close()
            tilt_servo.close()
            sensor.close()
        except Exception as e:
            print("Error during shutdown:", e)
        finally:
            time.sleep(0.5)
            exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    servo.angle = 90

    pan_servo.angle = 90

    # signal.signal(signal.SIGINT, signal_handler)

    
    try:
        trace()
    except KeyboardInterrupt:
        print("Dih")
        signal_handler(signal.SIGINT, signal_handler)
    
    signal_handler(signal.SIGINT, signal_handler)