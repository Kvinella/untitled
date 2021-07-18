import cv2
import numpy as np
import pyautogui
import threading
import time
from AutoHotPy import AutoHotPy
from InterceptionWrapper import *
q = 1
lb=("img/institut/lb/1.ipg","img/institut/lb/2.ipg","img/institut/lb/3.ipg","img/institut/lb/4.ipg","img/institut/lb/5.ipg",
    "img/institut/lb/6.ipg","img/institut/lb/7.ipg","img/institut/lb/8.ipg","img/institut/lb/9.ipg","img/institut/lb/10.ipg",
    "img/institut/lb/11.ipg")


class ClickClass:

    def __init__(self):
        # create AutoHotPy instance and set stop event handler
        self.auto = AutoHotPy()
        self.auto.registerExit(self.auto.ESC, self.auto.stop())

        # init threads
        self.auto_py_thread = threading.Thread(target=self.start_auto_py, args=())
    def start(self):
        # start threads
        self.auto_py_thread.start()
    def start_auto_py(self):
        self.auto.start()
    def recorded_macro(self):
        stroke = InterceptionMouseStroke()
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN
        self.auto.sendToDefaultMouse(stroke)
        stroke = InterceptionMouseStroke()
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_UP
        self.auto.sendToDefaultMouse(stroke)

    def click(self):
        self.recorded_macro()

    def moveTo_20(self, pt, w, h):
        self.auto.moveMouseToPosition(pt[0] + w -20, pt[1] + h - 20)
    def moveToPT(self, pt, w, h):
        self.auto.moveMouseToPosition(pt[0] + w, pt[1] + h)

    def moveTo(self, w, h):
        self.auto.moveMouseToPosition(w, h)


    def pressESC(self):
        self.auto.ESC.press()
    def pressF12(self):
        self.auto.F12.press()

    def pressW(self):
        self.auto.W.press()
    def pressA(self):
        self.auto.A.press()
    def pressS(self):
        self.auto.S.press()
    def pressD(self):
        self.auto.D.press()

    def press1(self):
        self.auto.N1.press()
    def press2(self):
        self.auto.N2.press()
    def press3(self):
        self.auto.N3.press()
    def press4(self):
        self.auto.N4.press()
    def press5(self):
        self.auto.N5.press()
    def press6(self):
        self.auto.N6.press()

    def pressE(self):
        self.auto.E.press()
    def pressR(self):
        self.auto.R.press()
    def pressT(self):
        self.auto.T.press()
    def pressF(self):
        self.auto.F.press()
    def pressC(self):
        self.auto.C.press()
    def pressV(self):
        self.auto.V.press()

    def upW(self):
        self.auto.W.up()
    def downW(self):
        self.auto.W.down()
    def upA(self):
        self.auto.A.up()
    def downA(self):
        self.auto.A.down()
    def upD(self):
        self.auto.D.up()
    def downD(self):
        self.auto.D.down()
    def upS(self):
        self.auto.S.up()
    def downS(self):
        self.auto.S.down()
    def downSHIST(self):
        self.auto.LEFT_SHIFT.down()
    def upSHIST(self):
        self.auto.LEFT_SHIFT.up()

    def pressSHIST(self):
        self.auto.LEFT_SHIFT.press()

click_class = ClickClass()
click_class.start()
time.sleep(2)
o = True

while o:

    x, y = pyautogui.size()  # получение координат монитора
    r = None
    while r is None:
        print('ожидаем квартал')
        ins = cv2.imread("img/institut/zk.jpg", 0)
        w, h = ins.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
        if flag:
            r = True

    click_class.downKey('S')  # бежим назад
    time.sleep(2.25)
    click_class.upKey('S')
    time.sleep(0.3)

    r = None
    while r is None:
        print('ожидаем к1')
        ins = cv2.imread("img/institut/one1.jpg", 0)
        w, h = ins.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)

        threshold = 0.7
        loc = np.where(res >= threshold)

        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
        if flag:
            r = True

    one = True
    if one:

        time.sleep(1)
        click_class.pressC() #баф
        time.sleep(1)

        click_class.downKey('D')  # бежим вправо
        time.sleep(0.3)
        click_class.upKey('D')
        time.sleep(0.3)

        click_class.downKey('W')
        click_class.downKey('SHIFT') #добегаем до стены
        time.sleep(2.8)
        click_class.upKey('W')
        click_class.upKey('SHIFT')
        time.sleep(0.5)

        click_class.downKey('A') #бежим вправо
        time.sleep(2.8)
        click_class.upKey('A')
        time.sleep(0.3)

        click_class.downKey('W') #добегаем до павуков
        click_class.downKey('SHIFT')
        time.sleep(2)
        click_class.upKey('W')
        click_class.upKey('SHIFT')
        time.sleep(0.3)

        click_class.pressKey('R') #убиваем павуков
        time.sleep(0.5)

        click_class.downKey('W')
        click_class.downKey('SHIFT') #добегаем до стены
        time.sleep(3.1)
        click_class.upKey('W')
        click_class.upKey('SHIFT')
        time.sleep(0.5)

        click_class.downKey('A') #бежим влево
        time.sleep(5.1)
        click_class.upKey('A')
        time.sleep(0.3)

        click_class.press5() #рушим павутину
        time.sleep(2)
        click_class.click()
        time.sleep(0.3)

        click_class.downKey('A') #бежим влево
        time.sleep(2)
        click_class.upKey('A')
        time.sleep(3)

        click_class.pressKey('R') #убиваем павуков
        time.sleep(0.5)

        click_class.downKey('A') #бежим влево
        time.sleep(4)
        click_class.upKey('A')
        time.sleep(0.3)

    r = None
    while r is None:
        print('ожидаем к2')
        ins = cv2.imread("img/institut/one2.jpg", 0)
        w, h = ins.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)

        threshold = 0.7
        loc = np.where(res >= threshold)

        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
        if flag:
            r = True

    one = True
    if one:
        time.sleep(1)

        click_class.downKey('W')
        click_class.downKey('SHIFT') #добегаем до стены
        time.sleep(3.6)
        click_class.upKey('W')
        click_class.upKey('SHIFT')
        time.sleep(0.5)

        click_class.downKey('D') #бежим вправо
        time.sleep(3.60)
        click_class.upKey('D')
        time.sleep(0.3)

        click_class.press6() #рушим павутину
        time.sleep(4)
        click_class.pressKey('R')
        time.sleep(0.3)

        click_class.downKey('D') #бежим вправо
        time.sleep(1.9)
        click_class.upKey('D')
        time.sleep(0.3)

        click_class.downKey('W')
        click_class.downKey('SHIFT') #добегаем до стены
        time.sleep(5.4)
        click_class.upKey('W')
        click_class.upKey('SHIFT')
        time.sleep(0.5)

        click_class.downKey('A') #бежим влево
        time.sleep(6)
        click_class.upKey('A')
        time.sleep(3)

        click_class.pressKey('R')
        time.sleep(0.3)

        click_class.downKey('S') #бежим назад
        time.sleep(2.5)
        click_class.upKey('S')
        time.sleep(0.3)

        click_class.downKey('A') #бежим влево
        time.sleep(5)
        click_class.upKey('A')
        time.sleep(0.3)

        click_class.press6() #рушим павутину
        time.sleep(4)

        click_class.downKey('A') #бежим влево
        time.sleep(4)
        click_class.upKey('A')
        time.sleep(3)

        click_class.pressKey('R')
        time.sleep(0.3)

        click_class.downKey('W') #бежим влево
        time.sleep(1)
        click_class.upKey('W')
        time.sleep(0.3)

        click_class.downKey('A') #бежим влево
        time.sleep(4)
        click_class.upKey('A')
        time.sleep(0.3)

    r = None
    while r is None:
        print('ожидаем загрузки')
        ins = cv2.imread("img/institut/pavyk.jpg", 0)
        w, h = ins.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
        if flag:
            r = True

    time.sleep(0.3)

    click_class.pressKey('ESC')

    r = None
    while r is None:
        print('ожидаем к3')
        ins = cv2.imread("img/institut/one3.jpg", 0)
        w, h = ins.shape[::-1]
        image = pyautogui.screenshot(region=(0, 0, x, y))
        img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        flag = False
        for pt in zip(*loc[::-1]):
            if pt is not None:
                flag = True
        if flag:
            r = True

    time.sleep(1)
    click_class.press1()
    time.sleep(2)

    click_class.downKey('W')
    click_class.downKey('SHIFT')  # добегаем до стены
    time.sleep(2)
    click_class.upKey('W')
    click_class.upKey('SHIFT')
    time.sleep(0.5)


    q = 0

