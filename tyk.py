import threading
from AutoHotPy import AutoHotPy
from InterceptionWrapper import *

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

    def recorded_macro1(self):
        stroke = InterceptionMouseStroke()
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN
        self.auto.sendToDefaultMouse(stroke)
        stroke = InterceptionMouseStroke()
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP
        self.auto.sendToDefaultMouse(stroke)


    def click(self):
        self.recorded_macro()

    def clickPKM(self):
        self.recorded_macro1()

    def moveTokDOSKE(self, pt, w, h):
        self.auto.moveMouseToPosition(pt[0] + w -20, pt[1] + h + 23)

    def moveToNZ(self, zx, zy):
        self.auto.moveMouseToPosition(zx, zy)

    def moveTo(self, pt, w, h):
        self.auto.moveMouseToPosition(pt[0] + w -20, pt[1] + h - 20)
    def moveTo20(self):
        self.auto.moveMouseToPosition(40,50)
    def moveTo550600(self):
        self.auto.moveMouseToPosition(550,600)
    def moveToD(self, pt, w, h):
        self.auto.moveMouseToPosition(pt[0] + w, pt[1] + h)

    def moveToR(self, w, h):
        self.auto.moveMouseToPosition(w, h)

    def downSPASE(self):
        self.auto.SPACE.down()
    def upSPASE(self):
        self.auto.SPACE.up()

    def pressSPASE(self):
        self.auto.SPACE.press()
    def pressEnter(self):
        self.auto.ENTER.press()
    def pressTAB(self):
        self.auto.TAB.press()
    def pressCTRL(self):
        self.auto.LEFT_CTRL.press()
    def pressESC(self):
        self.auto.ESC.press()


    def clickArrow(self):
        self.auto.DOWN_ARROW.press()



    def pressB(self):
        self.auto.B.press()
    def clickL(self):
        self.auto.L.press()
    def clickM(self):
        self.auto.M.press()


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

    def COMMA(self):
        self.auto.COMMA.press()

    def downCOMMA(self):
        self.auto.COMMA.down()

    def upCOMMA(self):
        self.auto.COMMA.up()

    def pressM(self):
        self.auto.M.press()
    def pressO(self):
        self.auto.O.press()

    def downCTRL(self):
        self.auto.LEFT_CTRL.down()

    def pressP(self):
        self.auto.P.press()

    def pressU(self):
        self.auto.U.press()




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
    def pressG(self):
        self.auto.G.press()

    def pressQ(self):
        self.auto.Q.press()



    def upE(self):
        self.auto.E.up()

    def downE(self):
        self.auto.E.down()


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
