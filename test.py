import time

import pyautogui

import functions
import tyk

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)

tyk.click_class.moveRelative(0, 400)
