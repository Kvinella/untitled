import cv2
import numpy as np
import pyautogui
import time
import tyk

def start():
    x, y = pyautogui.size()  # получение координат монитора
    tyk.click_class.start()
    time.sleep(3)
    o = 1
    n = 20

    while o <= n:
        r = None  # ожидание загрузки логова
        while r is None:
            time.sleep(0.5)
            exs = cv2.imread("data/institut/zab.png", 0)
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

        tyk.click_class.downS()
        time.sleep(3)
        tyk.click_class.upS()
