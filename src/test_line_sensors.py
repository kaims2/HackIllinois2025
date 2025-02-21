from scout.line_sensors import LineSensors
import time

line_sensors = LineSensors()


if __name__ == '__main__':

    while True:
        print('Far left: ', line_sensors.far_left_sensor.value)
        print('Middle left: ', line_sensors.middle_left_sensor.value)
        print('Middle right: ', line_sensors.middle_right_sensor.value)
        print('Far right: ', line_sensors.far_right_sensor.value)
        time.sleep(1)
