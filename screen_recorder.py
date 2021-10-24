from PIL import ImageGrab
from keyboard import is_pressed
from cv2 import VideoWriter, VideoWriter_fourcc, imshow, waitKey, destroyAllWindows, cvtColor, COLOR_BGR2RGB
from win32api import GetSystemMetrics
from numpy import array
from pyautogui import screenshot

width, height = GetSystemMetrics(0), GetSystemMetrics(1)

fourcc = VideoWriter_fourcc(*"XVID")
videoWriter = VideoWriter("out.avi", fourcc, 10, (width, height))

while not is_pressed("esc"):
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    # img = screenshot()
    array_img = array(img)
    image = cvtColor(array_img, COLOR_BGR2RGB)
    imshow("screen recorder",image)
    videoWriter.write(image)
    waitKey(10)
videoWriter.release()
destroyAllWindows()
