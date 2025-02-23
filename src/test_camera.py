from scout.camera import Camera
import time
camera = Camera()

if __name__ == '__main__':
    while True:
        camera.capture()
        print(camera.image_array)
        time.sleep(1)
