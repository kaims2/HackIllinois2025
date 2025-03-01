import gpiozero
from scout import constants
from scout.drivetrain import Drivetrain
from scout.line_sensors import LineSensors
import time
import signal

drivetrain = Drivetrain()
line_sensors = LineSensors()
	
#advance
def run(leftspeed, rightspeed):
    drivetrain.left_motor.forward(leftspeed)
    drivetrain.right_motor.forward(rightspeed)

#back
def back(leftspeed, rightspeed):
    drivetrain.left_motor.backward(leftspeed)
    drivetrain.right_motor.backward(rightspeed)

#left
def left(leftspeed, rightspeed):
    drivetrain.right_motor.forward(rightspeed)
    drivetrain.left_motor.forward(0)
    

#right
def right(leftspeed, rightspeed):
    drivetrain.right_motor.forward(0)
    drivetrain.left_motor.forward(leftspeed)

#turn left in place
def spin_left(leftspeed, rightspeed):
    drivetrain.left_motor.backward(leftspeed)
    drivetrain.right_motor.forward(rightspeed)

#turn right in place
def spin_right(leftspeed, rightspeed):
    drivetrain.left_motor.forward(leftspeed)
    drivetrain.right_motor.backward(rightspeed)

def stop():
    drivetrain.left_motor.forward(0)
    drivetrain.right_motor.backward(0)

if __name__ == '__main__':

    def signal_handler(sig, frame):
        drivetrain.left_motor.close()
        drivetrain.right_motor.close()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    fl_val = line_sensors.far_left_sensor.value
    fr_val = line_sensors.far_right_sensor.value
    ml_val = line_sensors.middle_left_sensor.value
    mr_val = line_sensors.middle_right_sensor.value


    while (fl_val or fr_val or ml_val or mr_val) == True:
        if fl_val == False and (mr_val == False or  fr_val == False):
            spin_left(0.5, 0.5)
            time.sleep(0.08)
        # 0 X X X
        #Left_sensor1 detected black line
        elif fl_val == False:
            spin_left(0.5, 0.5)
            time.sleep(0.08)
        elif ml_val == False and mr_val == True:
            left(0,0.5)
            time.sleep(0.08)
   
        #4 tracking pins level status
        # X 1 0 X  
        elif ml_val == True and mr_val == False:
            right(0.5, 0)
            time.sleep(0.08)
   
        #4 tracking pins level status
        # X 0 0 X
        elif ml_val == False and mr_val == False:
	        run(0.5, 0.5)
            time.sleep(0.08)




