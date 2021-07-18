import cv2
import numpy as np
import pyautogui
import tyk
import time

akk = ('BlueCoffee', 'obgect002', 'obgect003', 'obgect004')

o = 1 # цифра акка на котором сейчас бот
n = 3  # цифра всех акков

o1 = 0 # цифра персонажа на котором сейчас бот
n1 = 23 # цифра всех персонажей

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)

while o <= n:
    kolgrok = None
    ng = None

    r = None # ищем лог
    while r is None:
        print('ог')
        play = cv2.imread("data/ferma/log.jpg", 0)
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

    time.sleep(0.1)

    pyautogui.typewrite(akk[o])
    time.sleep(0.1)
    tyk.click_class.pressEnter()
    time.sleep(0.1)
    tyk.click_class.pressEnter()
    time.sleep(0.1)
    pyautogui.typewrite('n1n2n3')
    time.sleep(0.5)
    tyk.click_class.pressEnter()

    r = None # ищем ок
    while r is None:
        print('ищем ок')
        play = cv2.imread("data/ferma/log2.jpg", 0)
        w, h = play.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
        threshold = 0.6
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
        if flag:
            r = True
            tyk.click_class.pressEnter()



    r = None #ищем еграть
    while r is None:
        play = cv2.imread("data/ferma/egrat.jpg", 0)
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
                            tyk.click_class.moveTo(pt, w-10, h+10)
                            tyk.click_class.click()


            if flag:
                r = True

        g = 0 # тыкаем на клавишу вниз
        while g < o1:
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

        r = None  # ждем и тыкаем на ок, ищем куда загрузились в колдкрок или нг
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
                    flag = True #определяет куда загрузились
                    if flag == True:
                        play = cv2.imread("data/ferma/g/ch1k.jpg", 0)
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
                                kolgrok = True
                                flag = True
                        if flag:
                            r = True

                        play = cv2.imread("data/ferma/g/ch2k.jpg", 0)
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
                                kolgrok = True
                                flag = True
                        if flag:
                            r = True

                        play = cv2.imread("data/ferma/g/ch7n.jpg", 0)
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
                                ng = True
                                flag = True
                        if flag:
                            r = True

                        play = cv2.imread("data/ferma/g/ch3n.jpg", 0)
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
                                ng = True
                                flag = True
                        if flag:
                            r = True


                        play = cv2.imread("data/ferma/ok.jpg", 0)
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
                                    tyk.click_class.moveTo(pt, w - 10, h + 10)
                                    tyk.click_class.click()
                                    time.sleep(0.3)

                        if flag:
                            r = True

            if flag:
                r = True

        r = None  # ждем и тыкаем на закрыть
        while r is None:
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
                    if flag == True:
                        tyk.click_class.pressESC()
                        time.sleep(0.3)
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

            if flag:
                r = True

        #сюда добить галку и переключение
        if kolgrok == True:
            tyk.click_class.pressO()

            r = None  # ищем пати
            while r is None:
                play = cv2.imread("data/ferma/g/tp.jpg", 0)
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
                            tyk.click_class.moveTo(pt, w, h + 5)
                            tyk.click_class.click()
                            time.sleep(0.1)
                            tyk.click_class.click()

                if flag:
                    r = True

            r = None  # ищем вступить
            while r is None:
                play = cv2.imread("data/ferma/g/vst.jpg", 0)
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
                            time.sleep(0.1)

                if flag:
                    r = True

            r = None  # ищем выйти
            while r is None:
                play = cv2.imread("data/ferma/g/poka.jpg", 0)
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
                            time.sleep(0.1)

                if flag:
                    r = True

        if ng == True:

            tyk.click_class.pressP()
            r = None  # чек на крылья
            while r is None:
                play = cv2.imread("data/ferma/g/kost.jpg", 0)
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
                            time.sleep(0.1)

                            play = cv2.imread("data/ferma/g/krl.jpg", 0)
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
                                        tyk.click_class.clickPKM()
                                        time.sleep(0.1)

                r = True
                tyk.click_class.pressESC()

            ged = None
            iren = None
            k = True  # чек на квест
            if k == True:
                tyk.click_class.pressU()
                time.sleep(0.1)
                # переключаем на доступные задания
                play = cv2.imread("data/ferma/g/do.jpg", 0)
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
                            time.sleep(0.1)

                # открывае нг
                play = cv2.imread("data/ferma/g/ferma.jpg", 0)
                w, h = play.shape[::-1]
                image = pyautogui.screenshot(region=(0, 0, x, y))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
                threshold = 0.9
                loc = np.where(res >= threshold)
                flag = False
                for pt in zip(*loc[::-1]):
                    if pt is not None:
                        flag = True
                        if flag == True:
                            tyk.click_class.moveTo(pt, w, h)
                            tyk.click_class.click()
                            time.sleep(0.1)
                            tyk.click_class.click()
                            time.sleep(0.1)

                play = cv2.imread("data/ferma/g/kv.jpg", 0)
                w, h = play.shape[::-1]
                image = pyautogui.screenshot(region=(0, 0, x, y))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
                threshold = 0.9
                loc = np.where(res >= threshold)
                flag = False
                for pt in zip(*loc[::-1]):
                    if pt is not None:
                        flag = True
                        if flag == True:
                            tyk.click_class.moveTo(pt, w, h)
                            tyk.click_class.click()
                            time.sleep(0.1)
                            iren = True

                play = cv2.imread("data/ferma/g/kdedy.jpg", 0)
                w, h = play.shape[::-1]
                image = pyautogui.screenshot(region=(0, 0, x, y))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
                threshold = 0.9
                loc = np.where(res >= threshold)
                flag = False
                for pt in zip(*loc[::-1]):
                    if pt is not None:
                        flag = True
                        if flag == True:
                            ged = True

                print(iren, ged)

            tyk.click_class.pressESC()
            time.sleep(0.3)
            ded = False  # чеwaк на то где стоим
            if ded == False:
                play = cv2.imread("data/ferma/g/dedysh.jpg", 0)
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
                            ded = True
                        else:
                            ged = True

                print(ded)

            # бег до ирен если квест у нее не взят
            if iren == True:
                tyk.click_class.pressM()

                r = None  # ищем стрелку
                while r is None:
                    play = cv2.imread("data/ferma/g/vniz.jpg", 0)
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
                                tyk.click_class.moveTo(pt, w, h + 5)
                                tyk.click_class.click()
                                time.sleep(0.1)

                    if flag:
                        r = True

                r = None  # ищем портал
                while r is None:
                    play = cv2.imread("data/ferma/g/gate.jpg", 0)
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
                                tyk.click_class.moveTo(pt, w, h + 5)
                                tyk.click_class.click()
                                time.sleep(0.1)

                    if flag:
                        r = True

                r = None  # ищем сер
                while r is None:
                    play = cv2.imread("data/ferma/g/ser.jpg", 0)
                    w, h = play.shape[::-1]
                    image = pyautogui.screenshot(region=(0, 0, x, y))
                    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                    res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
                    threshold = 0.9
                    loc = np.where(res >= threshold)
                    flag = False
                    for pt in zip(*loc[::-1]):
                        if pt is not None:
                            flag = True

                    if flag:
                        r = True

                time.sleep(0.5)
                tyk.click_class.downCOMMA()
                time.sleep(0.3)

                tyk.click_class.upCOMMA()

                time.sleep(0.5)

                tyk.click_class.downA()
                time.sleep(0.1)
                tyk.click_class.upA()

                time.sleep(0.2)

                r = None  # ищем ирен
                while r is None:
                    print('ищу')
                    tyk.click_class.downW()

                    play = cv2.imread("data/ferma/g/Q.jpg", 0)
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
                        tyk.click_class.upW()
                        time.sleep(0.2)
                        tyk.click_class.pressQ()
                        r = True

                r = None  # ищем квест
                while r is None:
                    play = cv2.imread("data/ferma/g/pog.jpg", 0)
                    w, h = play.shape[::-1]
                    image = pyautogui.screenshot(region=(0, 0, x, y))
                    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                    res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
                    threshold = 0.9
                    loc = np.where(res >= threshold)
                    flag = False
                    for pt in zip(*loc[::-1]):
                        if pt is not None:
                            flag = True

                    if flag:
                        tyk.click_class.moveTo(pt, w, h + 5)
                        tyk.click_class.click()
                        time.sleep(0.1)

                        r = True

                r = None  # моя чудесная ферма
                while r is None:
                    play = cv2.imread("data/ferma/g/moz.jpg", 0)
                    w, h = play.shape[::-1]
                    image = pyautogui.screenshot(region=(0, 0, x, y))
                    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                    res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
                    threshold = 0.9
                    loc = np.where(res >= threshold)
                    flag = False
                    for pt in zip(*loc[::-1]):
                        if pt is not None:
                            flag = True

                    if flag:
                        tyk.click_class.moveTo(pt, w, h + 5)
                        tyk.click_class.click()
                        time.sleep(0.1)

                        r = True

                r = None  # моя чудесная ферма
                while r is None:
                    tyk.click_class.click()
                    time.sleep(0.2)
                    play = cv2.imread("data/ferma/g/oks.jpg", 0)
                    w, h = play.shape[::-1]
                    image = pyautogui.screenshot(region=(0, 0, x, y))
                    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                    res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
                    threshold = 0.9
                    loc = np.where(res >= threshold)
                    flag = False
                    for pt in zip(*loc[::-1]):
                        if pt is not None:
                            flag = True
                    if flag:
                        tyk.click_class.click()
                        ged = True
                        r = True

            # бег до деда если неправильно стоишь
            # бег до деда если неправильно стоишь
            print(iren, ged, ded)
            if ged == True:
                zy, zx = pyautogui.position()

                time.sleep(0.2)
                tyk.click_class.pressM()

                r = None  # ищем стрелку
                while r is None:
                    play = cv2.imread("data/ferma/g/vniz.jpg", 0)
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
                                tyk.click_class.moveTo(pt, w, h + 5)
                                tyk.click_class.click()
                                time.sleep(0.1)

                    if flag:
                        r = True

                r = None  # ищем портал
                while r is None:
                    play = cv2.imread("data/ferma/g/gate2.jpg", 0)
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
                                tyk.click_class.moveTo(pt, w, h + 10)
                                tyk.click_class.click()
                                time.sleep(0.1)

                    if flag:
                        r = True

                r = None  # ищем сер
                while r is None:
                    play = cv2.imread("data/ferma/g/ser.jpg", 0)
                    w, h = play.shape[::-1]
                    image = pyautogui.screenshot(region=(0, 0, x, y))
                    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                    res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
                    threshold = 0.9
                    loc = np.where(res >= threshold)
                    flag = False
                    for pt in zip(*loc[::-1]):
                        if pt is not None:
                            flag = True

                    if flag:
                        r = True

                tyk.click_class.pressCTRL()

                time.sleep(0.2)
                tyk.click_class.moveToNZ(zy, zx)
                time.sleep(0.2)

                tyk.click_class.pressCTRL()

                l = 0
                p = 1
                while l < p:
                    zy = zy - 17
                    tyk.click_class.moveToNZ(zy, zx)
                    time.sleep(0.1)
                    l = l + 1

                time.sleep(0.2)

                tyk.click_class.downA()
                time.sleep(3.7)
                tyk.click_class.upA()

                tyk.click_class.downW()
                time.sleep(5.6)
                tyk.click_class.upW()

                tyk.click_class.downA()
                time.sleep(1.6)
                tyk.click_class.upA()

                tyk.click_class.downW()
                time.sleep(5.5)
                tyk.click_class.upW()

                l = 0
                p = 1
                while l < p:
                    zy = zy + 17
                    tyk.click_class.moveToNZ(zy, zx)
                    time.sleep(0.1)
                    l = l + 1

                tyk.click_class.downW()
                time.sleep(7.4)
                tyk.click_class.upW()

            if ded == True:
                tyk.click_class.downA()
                time.sleep(0.3)
                tyk.click_class.upA()

                tyk.click_class.downW()
                time.sleep(0.2)
                tyk.click_class.upW()

            time.sleep(0.2)
            tyk.click_class.pressQ()

            r = None  # чек на квест и взятие если его нет
            while r is None:
                play = cv2.imread("data/ferma/g/zad.jpg", 0)
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
                            time.sleep(0.2)
                            tyk.click_class.moveTo(pt, w, h)
                            time.sleep(0.1)
                            tyk.click_class.click()

                            time.sleep(0.2)
                            print('ищу чудо')
                            play = cv2.imread("data/ferma/g/zudo.jpg", 0)
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
                                        time.sleep(0.2)
                                        tyk.click_class.moveTo(pt, w, h)
                                        time.sleep(0.1)
                                        tyk.click_class.click()
                                        time.sleep(0.1)
                                        tyk.click_class.click()
                                        time.sleep(0.1)
                                        tyk.click_class.click()
                                        time.sleep(0.1)
                                        tyk.click_class.click()
                                        time.sleep(0.1)

                                        play = cv2.imread("data/ferma/g/zad.jpg", 0)
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
                                                    time.sleep(0.1)
                                                    tyk.click_class.click()

                                                    play = cv2.imread("data/ferma/g/zem.jpg", 0)
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
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.click()
                                                                time.sleep(0.1)
                                                                tyk.click_class.pressQ()


                                                            else:
                                                                play = cv2.imread("data/ferma/g/nazad.jpg", 0)
                                                                w, h = play.shape[::-1]
                                                                image = pyautogui.screenshot(region=(0, 0, x, y))
                                                                img_rgb = cv2.cvtColor(np.array(image),
                                                                                       cv2.COLOR_RGB2BGR)
                                                                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                                                                res = cv2.matchTemplate(img_gray, play,
                                                                                        cv2.TM_CCOEFF_NORMED)
                                                                threshold = 0.8
                                                                loc = np.where(res >= threshold)
                                                                flag = False
                                                                for pt in zip(*loc[::-1]):
                                                                    if pt is not None:
                                                                        flag = True
                                                                        if flag == True:
                                                                            tyk.click_class.moveTo(pt, w, h)
                                                                            time.sleep(0.1)
                                                                            tyk.click_class.click()

                            play = cv2.imread("data/ferma/g/zem.jpg", 0)
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
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.click()
                                time.sleep(0.1)
                                tyk.click_class.pressQ()


                            else:
                                time.sleep(0.5)
                                print('ищу')
                                play = cv2.imread("data/ferma/g/nazad.jpg", 0)
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
                                            time.sleep(0.1)
                                            tyk.click_class.click()

                if flag:
                    r = True

            r = None  # тык магазин
            while r is None:
                play = cv2.imread("data/ferma/g/mag.jpg", 0)
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
                            time.sleep(0.1)
                if flag:
                    r = True

            r = None  # тык инструменты
            while r is None:
                play = cv2.imread("data/ferma/g/instr.jpg", 0)
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
                            tyk.click_class.moveTo(pt, w, h + 5)
                            tyk.click_class.click()
                            time.sleep(0.1)
                if flag:
                    r = True

            r = None  # купить лейку
            while r is None:
                play = cv2.imread("data/ferma/g/leiki.jpg", 0)
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
                            tyk.click_class.clickPKM()
                            time.sleep(0.1)
                if flag:
                    r = True

            r = None  # согласится
            while r is None:
                play = cv2.imread("data/ferma/g/otmena.jpg", 0)
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
                            time.sleep(0.1)
                            tyk.click_class.click()
                if flag:
                    r = True

            r = None  # тык на магазин семян
            while r is None:
                play = cv2.imread("data/ferma/g/semena.jpg", 0)
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
                            time.sleep(0.1)
                            tyk.click_class.click()
                if flag:
                    r = True

            r = None  # купить яблоки
            while r is None:
                play = cv2.imread("data/ferma/g/aple.jpg", 0)
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
                            tyk.click_class.moveTo(pt, w - 40, h)
                            time.sleep(0.1)
                            tyk.click_class.clickPKM()
                if flag:
                    r = True

            r = None  # согласится
            while r is None:
                play = cv2.imread("data/ferma/g/otmena.jpg", 0)
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
                            time.sleep(0.1)
                            tyk.click_class.click()
                if flag:
                    r = True

            time.sleep(1)
            tyk.click_class.pressESC()

        tyk.click_class.downA()
        time.sleep(3)
        tyk.click_class.upA()

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

        r = None  # ждем открыть после бежим к грядке
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
        time.sleep(3.3)
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

        time.sleep(0.2)

        vn = cv2.imread("data/ferma/serp.jpg", 0)
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

        r = None #поиск лопаты
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
                tyk.click_class.click()
                r = True

        r = None #поиск перчика
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
                    if flag:
                        tyk.click_class.moveTo(pt, w, h)
                        time.sleep(0.3)
                        tyk.click_class.click()
            if flag:
                r = True

        r = None #поиск посадить
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

        r = None #поиск лейки
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
            if flag:
                r = True



        #сюда потом поставить код на сбор
        time.sleep(4)
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

        o1 = o1 +1

    o = o+1

