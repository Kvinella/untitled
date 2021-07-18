import threading
import time

import functions
from AutoHotPy import AutoHotPy
from InterceptionWrapper import *


class ClickClass:

    started: bool = False

    auto: AutoHotPy

    SYMBOLS_KEYS: dict

    def __init__(self):

        # create AutoHotPy instance and set stop event handler
        self.auto = AutoHotPy()
        self.auto.registerExit(self.auto.NUMLOCK, self.stop)

        # init threads
        self.auto_py_thread = threading.Thread(target=self.start_auto_py, args=())

        self.SYMBOLS_KEYS = {
            ' ': self.auto.SPACE,
            'ENTER': self.auto.ENTER,
            'TAB': self.auto.TAB,
            'CTRL': self.auto.LEFT_CTRL,
            'ESC': self.auto.ESC,
            'COMMA': self.auto.COMMA,
            'A': self.auto.A,
            'B': self.auto.B,
            'C': self.auto.C,
            'D': self.auto.D,
            'E': self.auto.E,
            'F': self.auto.F,
            'G': self.auto.G,
            'H': self.auto.H,
            'I': self.auto.I,
            'J': self.auto.J,
            'K': self.auto.K,
            'L': self.auto.L,
            'M': self.auto.M,
            'N': self.auto.N,
            'O': self.auto.O,
            'P': self.auto.P,
            'Q': self.auto.Q,
            'R': self.auto.R,
            'S': self.auto.S,
            'T': self.auto.T,
            'U': self.auto.U,
            'V': self.auto.V,
            'W': self.auto.W,
            'X': self.auto.X,
            'Y': self.auto.Y,
            'Z': self.auto.Z,
            '0': self.auto.N0,
            '1': self.auto.N1,
            '2': self.auto.N2,
            '3': self.auto.N3,
            '4': self.auto.N4,
            '5': self.auto.N5,
            '6': self.auto.N6,
            '7': self.auto.N7,
            '8': self.auto.N8,
            '9': self.auto.N9,
            'DOWN_ARROW': self.auto.DOWN_ARROW
        }

    def start(self):
        if not self.started:
            self.auto_py_thread.start()
            self.started = True

    def start_auto_py(self):
        self.auto.start()

    def stop(self, *args):
        self.auto.stop()

    def click_lkm(self):
        stroke = InterceptionMouseStroke()
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN
        self.auto.sendToDefaultMouse(stroke)
        stroke = InterceptionMouseStroke()
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_UP
        self.auto.sendToDefaultMouse(stroke)

    def click_pkm(self):
        stroke = InterceptionMouseStroke()
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN
        self.auto.sendToDefaultMouse(stroke)
        stroke = InterceptionMouseStroke()
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP
        self.auto.sendToDefaultMouse(stroke)

    def click(self):
        self.click_lkm()

    def clickPKM(self):
        self.click_pkm()

    def moveToNZ(self, zx, zy):
        self.auto.moveMouseToPosition(zx, zy)

    def moveRelative(self, dx, dy):
        functions.send_relative_move(self.auto, 1, 1)
        functions.send_relative_move(self.auto, -1, -1)
        functions.send_relative_move(self.auto, dx, dy)

    def moveTo(self, pt, w, h):
        self.auto.moveMouseToPosition(pt[0] + w - 20, pt[1] + h - 20)

    def upKey(self, key: str):
        self.SYMBOLS_KEYS.get(key).up()

    def downKey(self, key: str):
        self.SYMBOLS_KEYS.get(key).down()

    def pressKey(self, key: str, pause: float = 0):
        if pause == 0:
            self.SYMBOLS_KEYS.get(key).press()
        else:
            self.SYMBOLS_KEYS.get(key).down()
            time.sleep(pause)
            self.SYMBOLS_KEYS.get(key).up()


click_class = ClickClass()
