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
        exs = cv2.imread("data/logova/any/feniks/feniks.jpg", 0)
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

    tyk.click_class.pressC()
    tyk.click_class.downD()
    time.sleep(1.7)
    tyk.click_class.upD()

    tyk.click_class.downW()
    time.sleep(1.5)
    tyk.click_class.upW()

    tyk.click_class.click()

    time.sleep(0.5)

    tyk.click_class.downA()
    time.sleep(1.6)
    tyk.click_class.upA()

    time.sleep(0.5)

    tyk.click_class.downW()
    tyk.click_class.downSHIST()
    time.sleep(8)
    tyk.click_class.upW()
    tyk.click_class.upSHIST()

    tyk.click_class.downA()
    time.sleep(1.6)
    tyk.click_class.upA()

    time.sleep(0.5)

    tyk.click_class.downW()
    tyk.click_class.pressSPASE()
    time.sleep(0.5)
    tyk.click_class.upW()

    time.sleep(0.2)

    tyk.click_class.downA()
    tyk.click_class.pressSPASE()
    time.sleep(0.5)
    tyk.click_class.upA()

    time.sleep(0.2)

    tyk.click_class.downA()
    tyk.click_class.pressSPASE()
    time.sleep(0.5)
    tyk.click_class.upA()

    time.sleep(0.2)

    tyk.click_class.downA()
    tyk.click_class.pressSPASE()
    time.sleep(0.5)
    tyk.click_class.upA()

    tyk.click_class.downA()
    time.sleep(10)
    tyk.click_class.upA()

    tyk.click_class.pressR()

    tyk.click_class.downA()
    time.sleep(10)
    tyk.click_class.upA()

    # второй босс
    tyk.click_class.downW()
    tyk.click_class.downSHIST()
    time.sleep(5)
    tyk.click_class.upW()
    tyk.click_class.downSHIST()

    tyk.click_class.downW()
    tyk.click_class.downSHIST()
    time.sleep(5)
    tyk.click_class.upW()
    tyk.click_class.upSHIST()

    tyk.click_class.pressR()
    time.sleep(0.7)
    tyk.click_class.pressT()

    tyk.click_class.downW()
    tyk.click_class.downSHIST()
    time.sleep(3)
    tyk.click_class.upW()
    tyk.click_class.upSHIST()

    # пргы-прыг
    time.sleep(0.7)
    tyk.click_class.downW()
    tyk.click_class.pressSPASE()
    time.sleep(0.5)
    tyk.click_class.upW()

    time.sleep(0.7)
    tyk.click_class.downW()
    tyk.click_class.pressSPASE()
    time.sleep(0.5)
    tyk.click_class.upW()

    time.sleep(0.7)
    tyk.click_class.downW()
    tyk.click_class.pressSPASE()
    time.sleep(0.5)
    tyk.click_class.upW()

    time.sleep(0.7)
    tyk.click_class.downW()
    tyk.click_class.pressSPASE()
    time.sleep(0.5)
    tyk.click_class.upW()

    #3-й босс
    tyk.click_class.downW()
    tyk.click_class.downSHIST()
    time.sleep(5)
    tyk.click_class.downSHIST()
    tyk.click_class.upW()

    tyk.click_class.downD()
    time.sleep(2)
    tyk.click_class.upD()

    tyk.click_class.pressR()
    time.sleep(0.7)
    tyk.click_class.pressT()

    tyk.click_class.downD()
    time.sleep(8)
    tyk.click_class.upD()

    #4-й босс
    tyk.click_class.downW()
    tyk.click_class.downSHIST()
    time.sleep(5)
    tyk.click_class.downSHIST()
    tyk.click_class.upW()

    time.sleep(1)
    tyk.click_class.clickESC()
    time.sleep(1)

    tyk.click_class.pressR()
    time.sleep(0.7)
    tyk.click_class.pressT()

    #открываем сундук
    tyk.click_class.downW()
    time.sleep(2.4)
    tyk.click_class.upW()

    tyk.click_class.downD()
    time.sleep(0.3)
    tyk.click_class.upD()
    tyk.click_class.click()

    tyk.click_class.pressG()
    time.sleep(0.3)
    tyk.click_class.pressG()
    time.sleep(0.3)
    tyk.click_class.pressG()
    time.sleep(0.3)
    tyk.click_class.pressG()
    time.sleep(0.3)
    tyk.click_class.pressG()
    time.sleep(0.3)
    tyk.click_class.pressG()
    time.sleep(0.3)
    tyk.click_class.pressG()
    time.sleep(0.3)
    tyk.click_class.pressG()
    time.sleep(0.3)
    tyk.click_class.pressG()


