# -*- coding: utf-8 -*-
import random
def init():
    source(findFile("scripts", "script_file_squish.py"))
    all()

def main():
    startApplication("ArmkApplication")
    clickButton(waitForObject(main_b)) #  Переход в режим "Основной"
    clickButton(waitForObject(measure_b)) #  Выбираю инструмент "Измерения"
    clickButton(waitForObject(measure_two_point_b)) #  Выбираю инструмент "Расстояние м/у двумя точками"
    
    x_list = [] #  Список для хранения значений координаты x
    y_list = [] #  Список для хранения значений координаты y
    k = 0
    m = 0  #  Счетчик пропусков из-за совпадений
    num = 20 #  Количество точек
    
    while k < num:
        x = random.randrange(104, 978, 25) #  randrange(start, stop, step)
        y = random.randrange(123, 690, 27)
        if x in x_list and y in y_list: #  Если пара x, y уже была, то точку ставить не нужно 
            m += 1
            continue
        else:
            x_list.append(x)
            y_list.append(y)
        #  Ставим точку с заданными координатами
        sendEvent("QMouseEvent", waitForObject(":mainWidget_cartography::MapWidgetImpl"), QEvent.MouseButtonPress, x, y, Qt.LeftButton, 1, 0)
        snooze(2)
        sendEvent("QMouseEvent", waitForObject(":mainWidget_cartography::MapWidgetImpl"), QEvent.MouseButtonRelease, x, y, Qt.LeftButton, 0, 0) 
        k += 1 #  Счетчик поставленных точек
    test.log("Количество итераций %d из %s" %(k, str(num)))


    #Делаю и сохраняю скриншот необходимой области экрана    
    photo_obj = waitForObject("{type='cartography::MapWidgetImpl' unnamed='1' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}")
    image = grabWidget(photo_obj)
    image.save("/home/screenshots/screenshot2.png", "PNG")
    
    test.log("Количество пропусков из-за совпадений", str(m)) 
