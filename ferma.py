import cv2
import numpy as np
import pyautogui
import time
import tyk

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)

o1 = 0 # цифра персонажа на котором сейчас бот
n1 = 15 # цифра всех персонажей



while o1 <= n1:
    r = None  # ищем полосу
    while r is None:
        play = cv2.imread("data/ferma/polosa.jpg", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True

        if flag:
            if o1 >= 1:
                tyk.click_class.moveTo(pt, w - 10, h + 10)
                tyk.click_class.click()

            r = True

    g = 0  # тыкаем на клавишу вниз
    while g <= o1:
        time.sleep(0.3)
        tyk.click_class.clickArrow()
        g = g + 1

    r = None  # тык на играть
    while r is None:
        play = cv2.imread("data/ferma/play.jpg", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
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
            r = True

    r = None  # ждем и тыкаем на ок
    while r is None:
        play = cv2.imread("data/ferma/ok.jpg", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
                if flag == True:
                    tyk.click_class.moveTo(pt, w - 10, h + 10)
                    tyk.click_class.click()
                    time.sleep(0.3)
        if flag:
            r = True


    r = None  # ждем загрузки
    while r is None:
        play = cv2.imread("data/ferma/zag.jpg", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
        if flag:
            r = True

    print('ищу закрыть')
    play = cv2.imread("data/ferma/close.jpg", 0)
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
    if flag:
        tyk.click_class.pressESC()
        time.sleep(0.5)


    tyk.click_class.downS()
    time.sleep(3)
    tyk.click_class.upS()

    r = None  # ждем и тыкаем на 13 инст
    while r is None:
        play = cv2.imread("data/ferma/instans.jpg", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.98
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
                if flag == True:
                    tyk.click_class.moveTo(pt, w, h)
                    time.sleep(0.1)
                    tyk.click_class.click()
                    time.sleep(0.1)
                    tyk.click_class.click()

        if flag:
            r = True


    r = None  # ждем прогрузки инста
    while r is None:
        play = cv2.imread("data/ferma/otk.jpg", 0)
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
        if flag:
            r = True



    zy, zx = pyautogui.position()

    tyk.click_class.downD()
    time.sleep(3.1)
    tyk.click_class.upD()

    tyk.click_class.downA()
    time.sleep(0.1)
    tyk.click_class.upA()

    tyk.click_class.downW()
    time.sleep(1.25)
    tyk.click_class.upW()

    tyk.click_class.downD()
    time.sleep(0.5)
    tyk.click_class.upD()

    tyk.click_class.pressCTRL()

    time.sleep(0.2)
    tyk.click_class.moveToNZ(zy, zx)
    time.sleep(0.2)

    tyk.click_class.pressCTRL()

    l = 0
    p = 4
    while l < p:
        zx = zx + 10
        tyk.click_class.moveToNZ(zy, zx)
        time.sleep(0.1)
        l = l + 1

    time.sleep(1)

    apl = False #чек на то вырасло ли что-то

    play = cv2.imread("data/ferma/apl.jpg", 0)
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
    if flag:
        tyk.click_class.click()
        apl = True
        r = True

    time.sleep(6)


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
    tyk.click_class.pressESC()

    r = None  # тык на еск
    while r is None:
        play = cv2.imread("data/ferma/ESC.jpg", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
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
            r = True

    r = None  # ожидаем вопрос
    while r is None:
        play = cv2.imread("data/ferma/vopros.jpg", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
                if flag == True:
                    tyk.click_class.click()
                    time.sleep(0.3)
        if flag:
            r = True

    o1 = o1 + 1

    if (o1 == 16):
        o1 = 0


