import time

import pyautogui

import functions
import tyk

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)


r = None
while r is None:
    check = functions.try_find_image("img/ferma/net.jng")  # чек на то вырасло ли что-то

    if check is not True:
        print('жду')

        time.sleep(60)
    else:
        print('выр')
        r = True