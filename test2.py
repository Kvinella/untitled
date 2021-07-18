import cv2
import numpy as np
import pyautogui
import time
import tyk

o = 0  # цифра акка на котором сейчас бот
n = 49  # цифра всех акков

o1 = 22 # цифра персонажа на котором сейчас бот
n1 = 23 # цифра всех персонажей

akk = ('obgect001', 'Персонаж 2', 'Персонаж 3', 'Персонаж 4', 'Персонаж 5', 'Персонаж 6', 'Персонаж 7'
       , 'Персонаж 8', 'Персонаж 9', 'Персонаж 10', 'Персонаж 11', 'Персонаж 12', 'Персонаж 13', 'Персонаж 14'
       , 'Персонаж 15', 'Персонаж 16', 'Персонаж 17', 'Персонаж 18', 'Персонаж 19', 'Персонаж 20')

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)

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

zy, zx = pyautogui.position()

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


tyk.click_class.downA()
time.sleep(1.7)
tyk.click_class.upA()

tyk.click_class.downW()
time.sleep(2.7)
tyk.click_class.upW()

tyk.click_class.pressB()

r = None  # тык на склад
while r is None:
       time.sleep(0.1)
       play = cv2.imread("data/ferma/ckl.jpg", 0)
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
              tyk.click_class.click()
              r = True


r = None  # тык на склад
while r is None:
       time.sleep(0.1)
       play = cv2.imread("data/ferma/per.jpg", 0)
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
       if flag:
              r = True

time.sleep(0.2)

tyk.click_class.pressESC()
time.sleep(0.2)
