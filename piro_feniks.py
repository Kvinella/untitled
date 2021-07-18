import cv2
import numpy as np
import pyautogui
import time
import tyk

x, y = pyautogui.size()
tyk.click_class.start()
time.sleep(3)


def feniks():

    r = None #ожидание загрузки логова
    while r is None:
        time.sleep(0.5)
        exs = cv2.imread("img/logova/any/feniks/feniks.jpg", 0)
        w2, h2 = exs.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, exs, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0, 0, 255), 2)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
        if flag:
            r = True

    time.sleep(0.5)

    tyk.click_class.pressKey('C')
    tyk.click_class.downKey('D')
    time.sleep(1.7)
    tyk.click_class.upKey('D')

    tyk.click_class.downKey('W')
    time.sleep(1.5)
    tyk.click_class.upKey('W')

    tyk.click_class.click()

    time.sleep(0.5)

    tyk.click_class.downKey('A')
    time.sleep(1.6)
    tyk.click_class.upKey('A')

    time.sleep(0.5)

    tyk.click_class.downKey('W')
    tyk.click_class.downKey('SHIFT')
    time.sleep(8)
    tyk.click_class.upKey('W')
    tyk.click_class.upKey('SHIFT')

    tyk.click_class.downKey('A')
    time.sleep(1.6)
    tyk.click_class.upKey('A')

    time.sleep(0.5)

    tyk.click_class.downKey('W')
    tyk.click_class.pressKey('SPACE')
    time.sleep(0.5)
    tyk.click_class.upKey('W')

    time.sleep(0.2)

    tyk.click_class.downKey('A')
    tyk.click_class.pressKey('SPACE')
    time.sleep(0.5)
    tyk.click_class.upKey('A')

    time.sleep(0.2)

    tyk.click_class.downKey('A')
    tyk.click_class.pressKey('SPACE')
    time.sleep(0.5)
    tyk.click_class.upKey('A')

    time.sleep(0.2)

    tyk.click_class.downKey('A')
    tyk.click_class.pressKey('SPACE')
    time.sleep(0.5)
    tyk.click_class.upKey('A')

    tyk.click_class.downKey('A')
    time.sleep(10)
    tyk.click_class.upKey('A')

    tyk.click_class.pressKey('R')

    tyk.click_class.downKey('A')
    time.sleep(10)
    tyk.click_class.upKey('A')

    # второй босс
    tyk.click_class.downKey('W')
    tyk.click_class.downKey('SHIFT')
    time.sleep(5)
    tyk.click_class.upKey('W')
    tyk.click_class.downKey('SHIFT')

    tyk.click_class.downKey('W')
    tyk.click_class.downKey('SHIFT')
    time.sleep(5)
    tyk.click_class.upKey('W')
    tyk.click_class.upKey('SHIFT')

    tyk.click_class.pressKey('R')
    time.sleep(0.7)
    tyk.click_class.pressKey('T')

    tyk.click_class.downKey('W')
    tyk.click_class.downKey('SHIFT')
    time.sleep(3)
    tyk.click_class.upKey('W')
    tyk.click_class.upKey('SHIFT')

    # пргы-прыг
    time.sleep(0.7)
    tyk.click_class.downKey('W')
    tyk.click_class.pressKey('SPACE')
    time.sleep(0.5)
    tyk.click_class.upKey('W')

    time.sleep(0.7)
    tyk.click_class.downKey('W')
    tyk.click_class.pressKey('SPACE')
    time.sleep(0.5)
    tyk.click_class.upKey('W')

    time.sleep(0.7)
    tyk.click_class.downKey('W')
    tyk.click_class.pressKey('SPACE')
    time.sleep(0.5)
    tyk.click_class.upKey('W')

    time.sleep(0.7)
    tyk.click_class.downKey('W')
    tyk.click_class.pressKey('SPACE')
    time.sleep(0.5)
    tyk.click_class.upKey('W')

    #3-й босс
    tyk.click_class.downKey('W')
    tyk.click_class.downKey('SHIFT')
    time.sleep(5)
    tyk.click_class.downKey('SHIFT')
    tyk.click_class.upKey('W')

    tyk.click_class.downKey('D')
    time.sleep(2)
    tyk.click_class.upKey('D')

    tyk.click_class.pressKey('R')
    time.sleep(0.7)
    tyk.click_class.pressKey('T')

    tyk.click_class.downKey('D')
    time.sleep(8)
    tyk.click_class.upKey('D')

    #4-й босс
    tyk.click_class.downKey('W')
    tyk.click_class.downKey('SHIFT')
    time.sleep(5)
    tyk.click_class.downKey('SHIFT')
    tyk.click_class.upKey('W')

    time.sleep(1)
    tyk.click_class.clickESC()
    time.sleep(1)

    tyk.click_class.pressKey('R')
    time.sleep(0.7)
    tyk.click_class.pressKey('T')

    #открываем сундук
    tyk.click_class.downKey('W')
    time.sleep(2.4)
    tyk.click_class.upKey('W')

    tyk.click_class.downKey('D')
    time.sleep(0.3)
    tyk.click_class.upKey('D')
    tyk.click_class.click()

    tyk.click_class.pressKey('G')
    time.sleep(0.3)
    tyk.click_class.pressKey('G')
    time.sleep(0.3)
    tyk.click_class.pressKey('G')
    time.sleep(0.3)
    tyk.click_class.pressKey('G')
    time.sleep(0.3)
    tyk.click_class.pressKey('G')
    time.sleep(0.3)
    tyk.click_class.pressKey('G')
    time.sleep(0.3)
    tyk.click_class.pressKey('G')
    time.sleep(0.3)
    tyk.click_class.pressKey('G')
    time.sleep(0.3)
    tyk.click_class.pressKey('G')


