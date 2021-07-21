import pyautogui
import time
import tyk
import functions
import random

#
# akk = ('BlueCoffee', 'obgect002', 'obgect003', 'obgect004', 'obgect005', 'obgect006', 'obgect007'
#        , 'obgect008', 'obgect009', 'obgect010', 'obgect011', 'obgect012', 'obgect013', 'obgect014'
#        , 'obgect001', 'obgect001', 'obgect001', 'obgect001', 'obgect001', 'obgect001')

x, y = pyautogui.size()  # получение координат монитора
tyk.click_class.start()
time.sleep(3)

o1 = 0  # цифра персонажа на котором сейчас бот
n1 = 16  # цифра всех персонажей

while o1 < n1:
    pt, w, h = functions.find_image("img/ferma/polosa.jpg")
    tyk.click_class.moveTo(pt, w - 10, h + 10)
    tyk.click_class.click()
    time.sleep(0.3)

    g = 0  # тыкаем на клавишу вниз
    while g < o1:
        tyk.click_class.pressKey('DOWN_ARROW')
        time.sleep(0.3)
        g += 1

    pt, w, h = functions.find_image("img/ferma/play.jpg")
    tyk.click_class.moveTo(pt, w, h)
    tyk.click_class.click()
    time.sleep(0.3)

    pt, w, h = functions.find_image("img/ferma/ok.jpg")  # ждем и тыкаем на ок
    tyk.click_class.moveTo(pt, w - 10, h + 10)
    tyk.click_class.click()
    time.sleep(0.3)

    functions.find_image("img/ferma/zag.jpg")  # ждем загрузки

    tyk.click_class.pressKey('S', 3)

    functions.find_image("img/ferma/instans.jpg")  # ждём меню с инстами

    channel = int(random.random() * 9) + 1

    for i in range(channel):
        tyk.click_class.pressKey('DOWN_ARROW')
        time.sleep(0.3)
    tyk.click_class.pressKey('ENTER')
    time.sleep(0.3)

    functions.find_image("img/ferma/otk.jpg")  # ждем прогрузки инста

    zy, zx = pyautogui.position()

    tyk.click_class.pressKey('D', 3.1)
    tyk.click_class.pressKey('A', 0.1)
    tyk.click_class.pressKey('W', 1.25)
    tyk.click_class.pressKey('D', 0.5)

    # Сброс положения курсора
    tyk.click_class.pressKey('CTRL')
    time.sleep(0.2)
    tyk.click_class.pressKey('CTRL')
    time.sleep(0.2)

    tyk.click_class.moveRelative(0, 400)

    time.sleep(1)

    check = functions.try_find_image("img/ferma/apl.jpg")  # чек на то вырасло ли что-то
    if check is not None:
        tyk.click_class.click()
        time.sleep(6)

    r = None
    while r is None:
        check = functions.try_find_image("img/ferma/net.jng")  # чек на то вырасло ли что-то
        if check is not True:
            time.sleep(60)
        else:
            r = True

    functions.find_image("img/ferma/lp.jpg")  # поиск лопаты
    time.sleep(1)
    tyk.click_class.click()
    time.sleep(0.3)

    pt, w, h = functions.find_image("img/ferma/perez.jpg")  # поиск перчика
    tyk.click_class.moveTo(pt, w, h)
    time.sleep(0.3)
    tyk.click_class.click()

    pt, w, h = functions.find_image("img/ferma/pos.jpg")  # поиск посадить
    tyk.click_class.moveTo(pt, w, h)
    time.sleep(0.3)
    tyk.click_class.click()

    functions.find_image("img/ferma/leika.jpg")  # поиск лейки
    time.sleep(0.3)
    tyk.click_class.click()

    if o1 == n1-1:
        time.sleep(300)

    time.sleep(8)
    tyk.click_class.pressKey('ESC')
    time.sleep(0.2)

    pt, w, h = functions.find_image("img/ferma/ESC.jpg")
    tyk.click_class.moveTo(pt, w, h)
    tyk.click_class.click()
    time.sleep(0.3)

    pt, w, h = functions.find_image("img/ferma/vopros.jpg")
    tyk.click_class.click()
    time.sleep(0.3)

    o1 += 1

    if o1 == n1:
        o1 = 0
