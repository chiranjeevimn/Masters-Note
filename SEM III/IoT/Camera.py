from picamera import PiCamera
import time
import datetime

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.vflip = True


camera.start_preview()

time.sleep(2)

Cd = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
camera.capture("/home/pi/desktop/" + Cd + ".jpg")
camera.stop_preview()
print("done")
