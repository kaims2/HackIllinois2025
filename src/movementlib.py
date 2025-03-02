import gpiozero
from scout import constants
from scout.drivetrain import Drivetrain
from scout.line_sensors import LineSensors
import time
import signal


def move(left, right):
    if left >= 0:
        drivetrain.left_motor.forward(left)
    else:
        drivetrain.left_motor.backward(-left)
    if right >= 0:
        drivetrain.right_motor.forward(right)
    else:
        drivetrain.right_motor.backward(-right)

def trace():

        def signal_handler(sig, frame):
            drivetrain.left_motor.close()
            drivetrain.right_motor.close()
            exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        f_speed, b_speed = 0.35, 0.55

        while True:

            current_time = time.time()
            if current_time - last_reset_time >= reset_interval:
                drivetrain.left_motor.stop()
                drivetrain.right_motor.stop()
                led.color = (1, 1, 1)
                time.sleep(0.5)
                led.off()
                last_reset_time = current_time
            
            det1 = not line_sensors.far_left_sensor.value #left most
            det2 = not line_sensors.middle_left_sensor.value
            det3 = not line_sensors.middle_right_sensor.value
            det4 = not line_sensors.far_right_sensor.value #right most

            print(det1, det2, det3, det4)

            # move(0.5 * det2 - 0.3 * det1, 0.5 * det3 - 0.3 * det4)
            # print(0.5 * det2 - 0.3 * det1, 0.5 * det3 - 0.3 * det4, '\n')

            move(f_speed * det2 - b_speed * det1, f_speed * det3 - b_speed * det4)
            print(f_speed * det2 - b_speed * det1, f_speed * det3 - b_speed * det4, '\n')

            if (f_speed * det2 - b_speed * det1 == 0) & (f_speed * det3 - b_speed * det4 == 0):
                move(-0.3, 0.3)

            time.sleep(0.1)


