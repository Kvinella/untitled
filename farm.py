import cv2
import numpy as np
import pyautogui
import time
import tyk

def start():

    o = 1
    n = 10
    p = 0
    g = 0

    name = ("data/bu/name/name1.jpg", "data/bu/name/name2.jpg", "data/bu/name/name3.jpg", "data/bu/name/name4.jpg",
            "data/bu/name/name5.jpg", "data/bu/name/name6.jpg", "data/bu/name/name7.jpg", "data/bu/name/name8.jpg",
            "data/bu/name/name9.jpg", "data/bu/name/name10.jpg", "data/bu/name/name11.jpg", "data/bu/name/name12.jpg",
            "data/bu/name/name13.jpg", "data/bu/name/name14.jpg", "data/bu/name/name15.jpg", "data/bu/name/name16.jpg",
            "data/bu/name/name17.jpg", "data/bu/name/name18.jpg", "data/bu/name/name19.jpg", "data/bu/name/name20.jpg")

    x, y = pyautogui.size()
    tyk.click_class.start()
    time.sleep(3)
    while o <= n:
        prof = None
        kardi = None
        feniks = None
        hran = None
        tymanka = None
        chiron = None
        daidalos = None
        granom = None
        manti = None
        mors = None

        l = True # заходим на персонажей, скрыла для удобства
        if l:
            r = None
            while r is None:
                play = cv2.imread("data/play.jpg", 0)
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
                vn = cv2.imread("data/vniz.jpg", 0)
                w, h = vn.shape[::-1]
                image = pyautogui.screenshot(region=(0, 0, x, y))
                img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                res = cv2.matchTemplate(img_gray, vn, cv2.TM_CCOEFF_NORMED)
                threshold = 0.8
                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                while g < (6 + p):
                    tyk.click_class.moveTo(pt, w, h)
                    tyk.click_class.click()
                    time.sleep(0.3)
                    g = g + 1
                g = 0
                p = p+1

            nam = cv2.imread(name[o], 0)
            w, h = nam.shape[::-1]
            image = pyautogui.screenshot(region=(0, 0, x, y))
            img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray, nam, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            tyk.click_class.moveTo(pt, w, h)

            time.sleep(1)
            tyk.click_class.click()
            tyk.click_class.click()
            time.sleep(0.5)
            tyk.click_class.click()

            r = None
            while r is None:
                vn = cv2.imread("data/ok.jpg", 0)
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
                vn = cv2.imread("data/close.jpg", 0)
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
                vn = cv2.imread("data/close.jpg", 0)
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

            tyk.click_class.clickL()
            time.sleep(1)

            r = None  # тык на квесты
            while r is None:
                play = cv2.imread("data/doska.jpg", 0)
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
            time.sleep(0.5)
            tyk.click_class.click()
            time.sleep(0.5)

        r = None #kardi
        while r is None:
            play = cv2.imread("data/logova/komar/kardi.jpg", 0)
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
                kardi = True
            r = True
        r = None #prof
        while r is None:
            play = cv2.imread("data/logova/komar/prof.jpg", 0)
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
                prof = True
            r = True
        
        r = None #feniks
        while r is None:
            play = cv2.imread("data/logova/any/feniks.jpg", 0)
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
                feniks = True
            r = True
        r = None #hran
        while r is None:
            play = cv2.imread("data/logova/any/hran.jpg", 0)
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
                hran = True
            r = True
        r = None #tymanka
        while r is None:
            play = cv2.imread("data/logova/any/tymanka.jpg", 0)
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
                tymanka = True
            r = True

        r = None #chiron
        while r is None:
            play = cv2.imread("data/logova/merka/chiron.jpg", 0)
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
                chiron = True
            r = True

        r = None #manti
        while r is None:
            play = cv2.imread("data/logova/yg/manti.jpg", 0)
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
                manti = True
            r = True
        r = None #mors
        while r is None:
            play = cv2.imread("data/logova/yg/mors.jpg", 0)
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
                mors = True
            r = True

        r = None #daidalos
        while r is None:
            play = cv2.imread("data/logova/padames/daidalos.jpg", 0)
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
                daidalos = True
            r = True
        r = None #granom
        while r is None:
            play = cv2.imread("data/logova/padames/granom.jpg", 0)
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
                granom = True
            r = True

        print('k', kardi, 'p', prof, 'f', feniks, 'h', hran, 't', tymanka, 'c', chiron,
              'm', manti, 'm2', mors, 'd', daidalos, 'g', granom)

        if (feniks == True) or (hran == True) or (tymanka == True):
            tyk.click_class.clickM()
            r = None   # ищем право нг
            while r is None:
                time.sleep(0.5)
                play = cv2.imread("data/logova/pravo.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

            r = None #ожидание телепорта
            while r is None:
                vn = cv2.imread("data/b.png", 0)
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

            tyk.click_class.downW()
            time.sleep(6)
            tyk.click_class.upW()

            r = None #выбираем ану арендель
            while r is None:
                play = cv2.imread("data/logova/any/any.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()
            r = None #тык на ОК
            while r is None:
                play = cv2.imread("data/ok.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()
            time.sleep(4)

            r = None #ожиданием загрузки ану
            while r is None:
                print('ожиданием загрузки ану')
                vn = cv2.imread("data/logova/any/meny.jpg", 0)
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

            flag = True #подходим к порталу
            if flag == True:
                time.sleep(0.3)
                tyk.click_class.pressTAB()
                time.sleep(0.3)

                tyk.click_class.downW()
                tyk.click_class.downA()
                time.sleep(2)
                tyk.click_class.upW()
                tyk.click_class.upA()

                tyk.click_class.downW()
                time.sleep(0.8)
                tyk.click_class.upW()

                tyk.click_class.downW()
                tyk.click_class.downA()
                time.sleep(4.8)
                tyk.click_class.upW()
                tyk.click_class.upA()

                tyk.click_class.downW()
                tyk.click_class.downD()
                time.sleep(0.6)
                tyk.click_class.upW()
                tyk.click_class.upD()

                tyk.click_class.downW()
                time.sleep(0.4)
                tyk.click_class.upW()

                tyk.click_class.downW()
                tyk.click_class.downD()
                time.sleep(1.2)
                tyk.click_class.upW()
                tyk.click_class.upD()

                tyk.click_class.downW()
                time.sleep(1.2)
                tyk.click_class.upW()

            if feniks == True:
                r = None  # ищем феникса
                while r is None:
                    vn = cv2.imread("data/logova/any/fenikslog.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()

                r = None  # тык на выбор
                while r is None:
                    vn = cv2.imread("data/logova/any/vibor.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()

                r = None  # тык вниз
                while r is None:
                    vn = cv2.imread("data/logova/any/vniz.jpg", 0)
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
                time.sleep(0.2)
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

                r = None  # тык низкий
                while r is None:
                    vn = cv2.imread("data/logova/any/nizk.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()

                r = None  # тык войти
                while r is None:
                    vn = cv2.imread("data/logova/any/voiti.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()

                if (o == 0) or (o == 1):
                    piro.feniks()

            if hran == True:
                r = None  # ищем храна
                while r is None:
                    vn = cv2.imread("data/logova/any/hranlog.jpg", 0)
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
                    time.sleep(0.2)
                    tyk.click_class.click()

                r = None  # тык на выбор
                while r is None:
                    vn = cv2.imread("data/logova/any/vibor.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()
                r = None  # тык вниз
                while r is None:
                    vn = cv2.imread("data/logova/any/vniz.jpg", 0)
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
                time.sleep(0.2)
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

                r = None  # тык низкий
                while r is None:
                    vn = cv2.imread("data/logova/any/nizk.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()

                r = None  # тык войти
                while r is None:
                    vn = cv2.imread("data/logova/any/voiti.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()

            if tymanka == True:
                r = None
                while r is None:
                    vn = cv2.imread("data/logova/any/tymankalog.jpg", 0)
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
                    time.sleep(0.2)
                    tyk.click_class.click()

                r = None  # тык на выбор
                while r is None:
                    vn = cv2.imread("data/logova/any/vibor.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()
                r = None  # тык вниз
                while r is None:
                    vn = cv2.imread("data/logova/any/vniz.jpg", 0)
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
                time.sleep(0.2)
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

                r = None  # тык низкий
                while r is None:
                    vn = cv2.imread("data/logova/any/nizk.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()

                r = None  # тык войти
                while r is None:
                    vn = cv2.imread("data/logova/any/voiti.jpg", 0)
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
                time.sleep(0.2)
                tyk.click_class.click()

        if (kardi == True) or (prof == True):
            tyk.click_class.clickM()
            r = None  # ищем низ нг
            while r is None:
                play = cv2.imread("data/logova/niz.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

            tyk.click_class.downW()
            time.sleep(10)
            tyk.click_class.upW()

            r = None
            while r is None:
                play = cv2.imread("data/logova/komar/km.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()
            r = None
            while r is None:
                play = cv2.imread("data/ok.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

        if (manti == True) or (mors == True):
            tyk.click_class.clickM()
            r = None  # ищем низ нг
            while r is None:
                play = cv2.imread("data/logova/niz.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

            tyk.click_class.downW()
            time.sleep(10)
            tyk.click_class.upW()

            r = None
            while r is None:
                play = cv2.imread("data/logova/yg/yp.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()
            r = None
            while r is None:
                play = cv2.imread("data/ok.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

        if (daidalos == True) or (granom == True):
            tyk.click_class.clickM()
            r = None  # ищем низ нг
            while r is None:
                play = cv2.imread("data/logova/levo.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

            tyk.click_class.downW()
            time.sleep(10)
            tyk.click_class.upW()

            r = None
            while r is None:
                play = cv2.imread("data/logova/padames/pd.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()
            r = None
            while r is None:
                play = cv2.imread("data/ok.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

        if (chiron == True):
            tyk.click_class.clickM()
            r = None  # ищем низ нг
            while r is None:
                play = cv2.imread("data/logova/levo.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

            tyk.click_class.downW()
            time.sleep(10)
            tyk.click_class.upW()

            r = None
            while r is None:
                play = cv2.imread("data/logova/padames/pd.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()
            r = None
            while r is None:
                play = cv2.imread("data/ok.jpg", 0)
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

            tyk.click_class.moveTo(pt, w, h)
            time.sleep(0.2)
            tyk.click_class.click()

        o = o + 1
