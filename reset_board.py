import cv2
import numpy as np
import pyautogui
import time
import tyk
import farm

def start():
    szet = 0
    kolvoKV = 0
    g = 0 #нужна чтобы тыкать вниз на экране выбора персонажей
    p = 0 #нужна чтобы тыкать вниз на экране выбора персонажей
    i = 0 #нужна для доски
    o = 0 #цифра персонажа на котором сейчас бот
    n = 19 #цифра всех персонажей
    j = 1 #когда-нибудь я пойму зачем эта переменная, но пока не знаю

    img = ("img/bu/kvest/1.jpg", "img/bu/kvest/2.jpg", "img/bu/kvest/3.jpg", "img/bu/kvest/4.jpg",
           "img/bu/kvest/5.jpg", "img/bu/kvest/6.jpg")
    k = ("img/bu/krest/k1.jpg", "img/bu/krest/k2.jpg", "img/bu/krest/k3.jpg", "img/bu/krest/k4.jpg",
         "img/bu/krest/k5.jpg", "img/bu/krest/k6.jpg")
    name = ("img/bu/name/name1.jpg", "img/bu/name/name2.jpg", "img/bu/name/name3.jpg", "img/bu/name/name4.jpg",
            "img/bu/name/name5.jpg", "img/bu/name/name6.jpg", "img/bu/name/name7.jpg", "img/bu/name/name8.jpg",
            "img/bu/name/name9.jpg", "img/bu/name/name10.jpg", "img/bu/name/name11.jpg", "img/bu/name/name12.jpg",
            "img/bu/name/name13.jpg", "img/bu/name/name14.jpg", "img/bu/name/name15.jpg", "img/bu/name/name16.jpg",
            "img/bu/name/name17.jpg", "img/bu/name/name18.jpg", "img/bu/name/name19.jpg", "img/bu/name/name20.jpg")
    nP=('Персонаж 1','Персонаж 2','Персонаж 3','Персонаж 4','Персонаж 5','Персонаж 6','Персонаж 7'
        ,'Персонаж 8','Персонаж 9','Персонаж 10','Персонаж 11','Персонаж 12','Персонаж 13','Персонаж 14'
        ,'Персонаж 15','Персонаж 16','Персонаж 17','Персонаж 18','Персонаж 19','Персонаж 20')

    tyk.click_class.start()
    time.sleep(2)

    while o <= n:
        e = True
        #тут скрыто для удобсва все что относится к выбору персонажа и закрытию всплывающих менюх
        if e:

            x, y = pyautogui.size() #получение координат монитора
            r = None
            while r is None:
                play = cv2.imread("img/play.jpg", 0)
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

            f = (o >= 6)
            if f:

                if g < (1 + p):
                    tyk.click_class.pressKey('DOWN_ARROW')
                    time.sleep(0.3)
                    g = g + 1

                g = 1
                p = p+1


            time.sleep(1)
            tyk.click_class.click()
            tyk.click_class.click()
            time.sleep(0.5)
            tyk.click_class.click()





            r = None
            while r is None:
                vn = cv2.imread("img/ok.jpg", 0)
                w, h = vn.shape[::-1]
                image = pyautogui.screenshot(region=(0, 0, x, y))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                res = cv2.matchTemplate(img_gray, vn, cv2.TM_CCOEFF_NORMED)
                threshold = 0.8
                loc = np.where(res >= threshold)
                flag = False
                for pt in zip(*loc[::-1]):
                    if pt is not None:
                        flag = True
                if flag:
                    r = True

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.5)
            tyk.click_class.click()

            r = None
            while r is None:
                vn = cv2.imread("img/close.jpg", 0)
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
                    r = True

            if r == True:
                tyk.click_class.clickESC()
                time.sleep(1)

                r = None
                vn = cv2.imread("img/close.jpg", 0)
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
                    r = True

                if r == True:
                    tyk.click_class.clickESC()
                    time.sleep(1)

        #проверка есть ли рядом доска
        r = None
        vn = cv2.imread("img/b.png", 0)
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
            r = True

        r = True #убрать если когда-нибудь понадобится перемещаться
        #перемешение к доске если персонаж не у доски
        if r == None:
            vn = cv2.imread("img/kd.png", 0)
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
                r = True
            tyk.click_class.moveTo(pt, w, h)

            #если мы в колдроке
            if r == True:
                print('нашел колдрок')
                tyk.click_class.click()

                r = None
                while r is None:
                    print('ищу галку')
                    tyk.click_class.press('0')
                    time.sleep(1)
                    play = cv2.imread("img/galka.png", 0)
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
                time.sleep(0.5)
                tyk.click_class.moveTo(pt, w, h)
                time.sleep(1)
                tyk.click_class.click()

                r = None
                while r is None:
                    print('ищу нг')
                    time.sleep(0.5)
                    play = cv2.imread("img/tpng.png", 0)
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

                tyk.click_class.moveTo(pt, w, h)
                tyk.click_class.click()
                tyk.click_class.click()

                r = None
                while r is None:
                    print('ищу вступить')
                    time.sleep(0.5)
                    play = cv2.imread("img/vstyp.png", 0)
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
                tyk.click_class.moveTo(pt, w, h)
                tyk.click_class.click()

                r = None
                while r is None:
                    print('ищу выход')
                    time.sleep(0.5)
                    play = cv2.imread("img/poka.png", 0)
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

                tyk.click_class.pressKey('CTRL')
                time.sleep(0.5)
                tyk.click_class.moveTo(pt, w, h)
                time.sleep(0.5)
                tyk.click_class.click()
                time.sleep(0.5)

            tyk.click_class.pressKey('M')

            r = None
            while r is None:
                print('поиск телепорта')
                vn = cv2.imread("img/tp.png", 0)
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
                    r = True

                time.sleep(1)
                print('тык на телепорт')
                tyk.click_class.moveToNZ(550, 600)
                time.sleep(1)

                tyk.click_class.click()

                r = None
                while r is None:
                    vn = cv2.imread("img/b.png", 0)
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
                        r = True

                tyk.click_class.downKey('S')
                time.sleep(0.2)
                tyk.click_class.upKey('S')

                tyk.click_class.downKey('A')
                time.sleep(3.2)
                tyk.click_class.upKey('A')

        #тут клик на B
        r = None
        while r is None:
            tyk.click_class.clickB()
            vn = cv2.imread("img/open.jpg", 0)
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
                r = True
                time.sleep(0.3)
                tyk.click_class.moveTo(pt, w, h)
                time.sleep(0.2)
                tyk.click_class.click()
                time.sleep(0.5)

        #ТУТ у нас часть работы с доской
        while i <= 5:
            time.sleep(1)
            kvest = cv2.imread(img[i], 0)
            w, h = kvest.shape[::-1]
            image = pyautogui.screenshot(region=(0, 0, x, y))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray, kvest, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.3)
            tyk.click_class.click()
            time.sleep(0.3)
            tyk.click_class.moveToNZ(40, 50)
            time.sleep(0.3)

            many = cv2.imread("img/perfect.jpg", 0)
            w, h = many.shape[::-1]
            image = pyautogui.screenshot(region=(0, 0, x, y))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray, many, cv2.TM_CCOEFF_NORMED)
            threshold = 0.95
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

            flag = True
            for pt in zip(*loc[::-1]):
                if pt is not None:
                    flag = False

            #поиск креста
            if flag:
                krest = cv2.imread(k[i], 0)
                w, h = krest.shape[::-1]
                image = pyautogui.screenshot(region=(0, 0, x, y))
                img_rgb1 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray1 = cv2.cvtColor(img_rgb1, cv2.COLOR_BGR2GRAY)
                res = cv2.matchTemplate(img_gray1, krest, cv2.TM_CCOEFF_NORMED)

                threshold = 0.86
                b = (i == 2) or (i == 3) or (i == 4) or (i == 5)
                if b:
                    threshold = 0.9

                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(img_rgb1, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

                tyk.click_class.moveTo(pt, w, h)
                time.sleep(0.1)
                tyk.click_class.click()
                time.sleep(0.3)

                vn = cv2.imread("img/ok.jpg", 0)
                w, h = vn.shape[::-1]
                image = pyautogui.screenshot(region=(0, 0, x, y))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                res = cv2.matchTemplate(img_gray, vn, cv2.TM_CCOEFF_NORMED)
                threshold = 0.8
                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

                tyk.click_class.moveToNZ(pt[0] + w, pt[1] + h)
                time.sleep(0.5)
                tyk.click_class.click()
                tyk.click_class.click()
                tyk.click_class.moveToNZ(40, 50)
                time.sleep(0.2)

            if flag == False:
                kolvoKV = kolvoKV + 1

            i = i + 1
            if i == 6:
                if kolvoKV == 6:
                     szet = szet + 1
                tyk.click_class.clickESC()
                time.sleep(1)

        #тут клик на ESC
        r = None
        while r is None:
            tyk.click_class.clickESC()
            time.sleep(0.5)
            exs = cv2.imread("img/exs.jpg", 0)
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

        print('кол-во квестов на', nP[o], kolvoKV)

        i = 0
        o = o + 1
        f = 20 == o
        kolvoKV = 0
        if f:
            print('кол-во персонажей с фулл квестами', szet)
            szet = 0
            o = 0
            p = 0
            j = j+1
            time.sleep(60)

        tyk.click_class.moveTo(pt, w, h)
        time.sleep(0.5)
        tyk.click_class.click()
        time.sleep(2)
        tyk.click_class.click()