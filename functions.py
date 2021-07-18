import cv2
import numpy as np
import pyautogui

from AutoHotPy import AutoHotPy
from InterceptionWrapper import InterceptionMouseStroke, InterceptionMouseState, InterceptionMouseFlag


def find_image(img: str):
    x, y = pyautogui.size()  # получение координат монитора
    while True:  # ищем картинку
        ans = try_find_image(img, x, y)
        if ans is not None:
            return ans


def try_find_image(img: str, x: int = 0, y: int = 0):
    if x == 0 and y == 0:
        x, y = pyautogui.size()  # получение координат монитора
    play = cv2.imread(img, 0)
    w, h = play.shape[::-1]
    image = pyautogui.screenshot(region=(0, 0, x, y))
    img_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, play, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        if pt is not None:
            return [pt, w, h]
    return None

def send_relative_move(auto_hot_py: AutoHotPy, x: float, y: float):
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = int(x)
    stroke.y = int(y)
    auto_hot_py.sendToDefaultMouse(stroke)
