import cv2
import numpy as np
import pyautogui
import tyk
import time
import var1
x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)

print('ожидаем вар1')
ins = cv2.imread('data/ferma/var1.jpg', 0)
w, h = ins.shape[::-1]
image = pyautogui.screenshot(region=(0, 0, x, y))
img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)

flag = False
for pt in zip(*loc[::-1]):
    if pt is not None:
        flag = True
if flag:
    tyk.click_class.recorded_macro1()

print('ожидаем вар1')
ins = cv2.imread('data/ferma/var1.jpg', 0)
w, h = ins.shape[::-1]
image = pyautogui.screenshot(region=(0, 0, x, y))
img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)

flag = False
for pt in zip(*loc[::-1]):
    if pt is not None:
        flag = True
if flag:
    print('ожидаем вар1')

    tyk.click_class.recorded_macro1()


print('ожидаем вар2')
ins = cv2.imread('data/ferma/var2.jpg', 0)
w, h = ins.shape[::-1]
image = pyautogui.screenshot(region=(0, 0, x, y))
img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)

flag = False
for pt in zip(*loc[::-1]):
    if pt is not None:
        flag = True
if flag:
    print('ожидаем вар1')

    tyk.click_class.recorded_macro2()


print('ожидаем вар3')
ins = cv2.imread('data/ferma/var3.jpg', 0)
w, h = ins.shape[::-1]
image = pyautogui.screenshot(region=(0, 0, x, y))
img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)

flag = False
for pt in zip(*loc[::-1]):
    if pt is not None:
        flag = True
if flag:
    print('ожидаем вар1')

    tyk.click_class.recorded_macro3()


print('ожидаем вар4')
ins = cv2.imread('data/ferma/var4.jpg', 0)
w, h = ins.shape[::-1]
image = pyautogui.screenshot(region=(0, 0, x, y))
img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
threshold = 0.96
loc = np.where(res >= threshold)

flag = False
for pt in zip(*loc[::-1]):
    if pt is not None:
        flag = True
if flag:
    print('ожидаем вар1')

    tyk.click_class.recorded_macro4()


print('ожидаем вар5')
ins = cv2.imread('data/ferma/var5.jpg', 0)
w, h = ins.shape[::-1]
image = pyautogui.screenshot(region=(0, 0, x, y))
img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, ins, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)

flag = False
for pt in zip(*loc[::-1]):
    if pt is not None:
        flag = True
if flag:
    print('ожидаем вар1')

    tyk.click_class.recorded_macro5()
