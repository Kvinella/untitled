import cv2
import numpy as np
import pyautogui
import tyk
import time

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)


zy, zx = pyautogui.position()

time.sleep(0.2)
tyk.click_class.moveToNZ(zy, zx+100)
time.sleep(0.2)