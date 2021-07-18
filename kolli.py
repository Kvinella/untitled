import cv2
import numpy as np
import pyautogui
import tyk
import time

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)

r = None
while r is None:
    n = None # ищем плау
    while n is None:
        time.sleep(3)
        print('ог')
        play = cv2.imread("gotov.png", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
                if flag == True:
                    tyk.click_class.moveTo(pt, w, h)
                    tyk.click_class.click()
                    time.sleep(0.3)

        if flag:
            n = True
            print('ог')
            play = cv2.imread("v.png", 0)
            w, h = play.shape[::-1]
            image = pyautogui.screenshot(region=(0, 0, x, y))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where(res >= threshold)
            flag = False
            for pt in zip(*loc[::-1]):
                if pt is not None:
                    flag = True
                    if flag == True:
                        tyk.click_class.click()
                        time.sleep(0.3)

        else:

            tyk.click_class.press1()
            time.sleep(1)
