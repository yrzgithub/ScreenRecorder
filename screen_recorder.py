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


#second way

from pyautogui import screenshot
import cv2
from numpy import array
from keyboard import is_pressed
from win32api import GetSystemMetrics as get

width, height = get(0), get(1)

four_cc = cv2.VideoWriter_fourcc(*"XVID")
video_writer = cv2.VideoWriter("output.avi", four_cc,5, (width, height))

while not is_pressed("esc"):
    img = screenshot()
    img_array = array(img)
    cv2.imshow(winname="Screen recorder", mat=img_array)
    video_writer.write(img_array)
    cv2.waitKey(10)

cv2.destroyAllWindows()