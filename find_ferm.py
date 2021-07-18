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
        play = cv2.imread("img/ferma/log.jpg", 0)
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
    tyk.click_class.pressKey('ENTER')
    time.sleep(0.1)
    tyk.click_class.pressKey('ENTER')
    time.sleep(0.1)
    pyautogui.typewrite('n1n2n3')
    time.sleep(0.5)
    tyk.click_class.pressKey('ENTER')

    r = None # ищем ок
    while r is None:
        print('ищем ок')
        play = cv2.imread("img/ferma/log2.jpg", 0)
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
            tyk.click_class.pressKey('ENTER')



    r = None #ищем еграть
    while r is None:
        play = cv2.imread("img/ferma/egrat.jpg", 0)
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
            play = cv2.imread("img/ferma/polosa.jpg", 0)
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
            tyk.click_class.pressKey('DOWN_ARROW')
            g = g + 1

        r = None  # тык на играть
        while r is None:
            play = cv2.imread("img/ferma/play.jpg", 0)
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
            play = cv2.imread("img/ferma/ok.jpg", 0)
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
                        play = cv2.imread("img/ferma/g/ch1k.jpg", 0)
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

                        play = cv2.imread("img/ferma/g/ch2k.jpg", 0)
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

                        play = cv2.imread("img/ferma/g/ch7n.jpg", 0)
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

                        play = cv2.imread("img/ferma/g/ch3n.jpg", 0)
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


                        play = cv2.imread("img/ferma/ok.jpg", 0)
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
            play = cv2.imread("img/ferma/close.jpg", 0)
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
                        tyk.click_class.pressKey('ESC')
                        time.sleep(0.3)
                        play = cv2.imread("img/ferma/close.jpg", 0)
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
                            tyk.click_class.pressKey('ESC')

            if flag:
                r = True

        #сюда добить галку и переключение
        if kolgrok == True:
            tyk.click_class.press('0')

            r = None  # ищем пати
            while r is None:
                play = cv2.imread("img/ferma/g/tp.jpg", 0)
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
                play = cv2.imread("img/ferma/g/vst.jpg", 0)
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
                play = cv2.imread("img/ferma/g/poka.jpg", 0)
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

            tyk.click_class.press('P')
            r = None  # чек на крылья
            while r is None:
                play = cv2.imread("img/ferma/g/kost.jpg", 0)
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

                            play = cv2.imread("img/ferma/g/krl.jpg", 0)
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
                tyk.click_class.pressKey('ESC')

            ged = None
            iren = None
            k = True  # чек на квест
            if k == True:
                tyk.click_class.press('U')
                time.sleep(0.1)
                # переключаем на доступные задания
                play = cv2.imread("img/ferma/g/do.jpg", 0)
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
                play = cv2.imread("img/ferma/g/ferma.jpg", 0)
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

                play = cv2.imread("img/ferma/g/kv.jpg", 0)
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

                play = cv2.imread("img/ferma/g/kdedy.jpg", 0)
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

            tyk.click_class.pressKey('ESC')
            time.sleep(0.3)
            ded = False  # чеwaк на то где стоим
            if ded == False:
                play = cv2.imread("img/ferma/g/dedysh.jpg", 0)
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
                tyk.click_class.press('M')

                r = None  # ищем стрелку
                while r is None:
                    play = cv2.imread("img/ferma/g/vniz.jpg", 0)
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
                    play = cv2.imread("img/ferma/g/gate.jpg", 0)
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
                    play = cv2.imread("img/ferma/g/ser.jpg", 0)
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
                tyk.click_class.pressKey('COMMA', 0.3)

                time.sleep(0.5)

                tyk.click_class.downKey('A')
                time.sleep(0.1)
                tyk.click_class.upKey('A')

                time.sleep(0.2)

                r = None  # ищем ирен
                while r is None:
                    print('ищу')
                    tyk.click_class.downKey('W')

                    play = cv2.imread("img/ferma/g/Q.jpg", 0)
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
                        tyk.click_class.upKey('W')
                        time.sleep(0.2)
                        tyk.click_class.press('Q')
                        r = True

                r = None  # ищем квест
                while r is None:
                    play = cv2.imread("img/ferma/g/pog.jpg", 0)
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
                    play = cv2.imread("img/ferma/g/moz.jpg", 0)
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
                    play = cv2.imread("img/ferma/g/oks.jpg", 0)
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
                tyk.click_class.press('M')

                r = None  # ищем стрелку
                while r is None:
                    play = cv2.imread("img/ferma/g/vniz.jpg", 0)
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
                    play = cv2.imread("img/ferma/g/gate2.jpg", 0)
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
                    play = cv2.imread("img/ferma/g/ser.jpg", 0)
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

                tyk.click_class.pressKey('CTRL')

                time.sleep(0.2)
                tyk.click_class.moveToNZ(zy, zx)
                time.sleep(0.2)

                tyk.click_class.pressKey('CTRL')

                l = 0
                p = 1
                while l < p:
                    zy = zy - 17
                    tyk.click_class.moveToNZ(zy, zx)
                    time.sleep(0.1)
                    l = l + 1

                time.sleep(0.2)

                tyk.click_class.downKey('A')
                time.sleep(3.7)
                tyk.click_class.upKey('A')

                tyk.click_class.downKey('W')
                time.sleep(5.6)
                tyk.click_class.upKey('W')

                tyk.click_class.downKey('A')
                time.sleep(1.6)
                tyk.click_class.upKey('A')

                tyk.click_class.downKey('W')
                time.sleep(5.5)
                tyk.click_class.upKey('W')

                l = 0
                p = 1
                while l < p:
                    zy = zy + 17
                    tyk.click_class.moveToNZ(zy, zx)
                    time.sleep(0.1)
                    l = l + 1

                tyk.click_class.downKey('W')
                time.sleep(7.4)
                tyk.click_class.upKey('W')

            if ded == True:
                tyk.click_class.downKey('A')
                time.sleep(0.3)
                tyk.click_class.upKey('A')

                tyk.click_class.downKey('W')
                time.sleep(0.2)
                tyk.click_class.upKey('W')

            time.sleep(0.2)
            tyk.click_class.pressKey('Q')

            r = None  # чек на квест и взятие если его нет
            while r is None:
                play = cv2.imread("img/ferma/g/zad.jpg", 0)
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
                            play = cv2.imread("img/ferma/g/zudo.jpg", 0)
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

                                        play = cv2.imread("img/ferma/g/zad.jpg", 0)
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

                                                    play = cv2.imread("img/ferma/g/zem.jpg", 0)
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
                                                                tyk.click_class.pressKey('Q')


                                                            else:
                                                                play = cv2.imread("img/ferma/g/nazad.jpg", 0)
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

                            play = cv2.imread("img/ferma/g/zem.jpg", 0)
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
                                tyk.click_class.pressKey('Q')


                            else:
                                time.sleep(0.5)
                                print('ищу')
                                play = cv2.imread("img/ferma/g/nazad.jpg", 0)
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
                play = cv2.imread("img/ferma/g/mag.jpg", 0)
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
                play = cv2.imread("img/ferma/g/instr.jpg", 0)
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
                play = cv2.imread("img/ferma/g/leiki.jpg", 0)
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
                play = cv2.imread("img/ferma/g/otmena.jpg", 0)
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
                play = cv2.imread("img/ferma/g/semena.jpg", 0)
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
                play = cv2.imread("img/ferma/g/aple.jpg", 0)
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
                play = cv2.imread("img/ferma/g/otmena.jpg", 0)
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
            tyk.click_class.pressKey('ESC')

        tyk.click_class.downKey('A')
        time.sleep(3)
        tyk.click_class.upKey('A')

        r = None  # ждем и тыкаем на 13 инст
        while r is None:
            play = cv2.imread("img/ferma/instans.jpg", 0)
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
            play = cv2.imread("img/ferma/otk.jpg", 0)
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

        tyk.click_class.downKey('D')
        time.sleep(3.3)
        tyk.click_class.upKey('D')

        tyk.click_class.downKey('A')
        time.sleep(0.1)
        tyk.click_class.upKey('A')

        tyk.click_class.downKey('W')
        time.sleep(1.25)
        tyk.click_class.upKey('W')

        tyk.click_class.downKey('D')
        time.sleep(0.5)
        tyk.click_class.upKey('D')

        tyk.click_class.pressKey('CTRL')

        time.sleep(0.2)
        tyk.click_class.moveToNZ(zy, zx)
        time.sleep(0.2)

        tyk.click_class.pressKey('CTRL')

        l = 0
        p = 4
        while l < p:
            zx = zx + 10
            tyk.click_class.moveToNZ(zy, zx)
            time.sleep(0.1)
            l = l + 1

        time.sleep(0.2)

        vn = cv2.imread("img/ferma/serp.jpg", 0)
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
            vn = cv2.imread("img/ferma/lp.jpg", 0)
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
            vn = cv2.imread("img/ferma/perez.jpg", 0)
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
            vn = cv2.imread("img/ferma/pos.jpg", 0)
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
            vn = cv2.imread("img/ferma/leika.jpg", 0)
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
        tyk.click_class.pressKey('ESC')


        r = None  # тык на еск
        while r is None:
            play = cv2.imread("img/ferma/ESC.jpg", 0)
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
            play = cv2.imread("img/ferma/vopros.jpg", 0)
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

