import cv2
import numpy as np
import pyautogui
import time
import tyk

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)

r = None  # поиск лопаты
while r is None:
    vn = cv2.imread("data/ferma/lp.jpg", 0)
    w, h = vn.shape[::-1]
    image = pyautogui.screenshot(region=(0, 0, x, y))
    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, vn, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    flag = False
    for pt in zip(*loc[::-1]):
        if pt is not None:
            flag = True
    if flag:
        time.sleep(1)
        tyk.click_class.click()
        time.sleep(0.3)

        r = None  # поиск перчика
        while r is None:
            vn = cv2.imread("data/ferma/perez.jpg", 0)
            w, h = vn.shape[::-1]
            image = pyautogui.screenshot(region=(0, 0, x, y))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray, vn, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            flag = False
            for pt in zip(*loc[::-1]):
                if pt is not None:
                    flag = True
                    tyk.click_class.moveTo(pt, w, h)

            if flag:
                time.sleep(0.3)
                tyk.click_class.click()
                r = True

        r = None  # поиск посадить
        while r is None:
            vn = cv2.imread("data/ferma/pos.jpg", 0)
            w, h = vn.shape[::-1]
            image = pyautogui.screenshot(region=(0, 0, x, y))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray, vn, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            flag = False
            for pt in zip(*loc[::-1]):
                if pt is not None:
                    flag = True
                    if flag:
                        tyk.click_class.moveTo(pt, w, h)
                        time.sleep(0.3)
                        tyk.click_class.click()
            if flag:
                r = True

        r = None  # поиск лейки
        while r is None:
            vn = cv2.imread("data/ferma/leika.jpg", 0)
            w, h = vn.shape[::-1]
            image = pyautogui.screenshot(region=(0, 0, x, y))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray, vn, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            flag = False
            for pt in zip(*loc[::-1]):
                if pt is not None:
                    flag = True
            if flag:
                time.sleep(0.3)
                tyk.click_class.click()
                r = True

    r = True

time.sleep(7)
time.sleep(2)
tyk.click_class.pressESC()

