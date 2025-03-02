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

def Move_Around():
    distances = []
    for angle in range(30, 150, 1):
        servo.angle = angle
        time.sleep(0.03)
        distance = sensor.distance
        distances.append(distance)
    plt.plot(range(30, 150, 1), distances, 'o-')
    plt.savefig("Test.png")
    # Define sensor tolerance and safe distance threshold
    DIST_TOLERANCE = 0.08
    SAFE_DISTANCE = 0.95

    turn_left = 0 if np.arange(30,150)[np.argmax(distances)] < 90 else 1
    if turn_left:
        move(-0.5, 0.5)
        servo.angle = 30
        time.sleep(0.6)
        move(0, 0)
    else:
        move(0.5, -0.5)
        servo.angle = 150
        time.sleep(0.6)
        move(0, 0)
        
    while True:
        init_dist = sensor.distance
        move(0.3, 0.3)
        time.sleep(0.8)
        move(0.4 * turn_left - 0.3 * ((turn_left + 1) % 2),
            0.4 * ((turn_left + 1) % 2) - 0.3 * turn_left)
        # Wait until sensor distance has changed by more than the tolerance or exceeds safe distance
        while sensor.distance >= init_dist - DIST_TOLERANCE and sensor.distance <= SAFE_DISTANCE:
            time.sleep(0.01)
        time.sleep(0.1)
        move(0, 0)
        if sensor.distance >= SAFE_DISTANCE:
            move(0.4 * ((turn_left + 1) % 2) - 0.3 * turn_left,
                0.4 * turn_left - 0.3 * ((turn_left + 1) % 2))
            time.sleep(1.5)
        move(0, 0)
        reset()
    return


if __name__ == '__main__':

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

    ind = 0
    try:
        while True:
            distance = sensor.distance
            servo.angle = 90
            move(0.35, -0.35)
            if distance < 0.4:
                move(0, 0)
                human = Check_Human(distance)
                if human:
                    print("Human")
                    Move_Around()
                    time.sleep(2)
                    break
                else:
                    print("Object")
                    Move_Around()
                    break
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Dih")
        signal_handler(signal.SIGINT, signal_handler)
    
    signal_handler(signal.SIGINT, signal_handler)