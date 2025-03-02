from scout.camera import Camera
import time
import matplotlib.pyplot as plt
camera = Camera()

if __name__ == '__main__':
    while True:
        camera.capture()
        print(camera.image_array)
        plt.imshow(camera.image_array)
        plt.savefig("Test.png")
        time.sleep(2)

