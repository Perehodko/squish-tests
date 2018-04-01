# -*- coding: utf-8 -*-
#####################################################################
# ОБЩЕЕ
#####################################################################

def all():
    global route_b
    global okButton
    global b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, b_0, plus_minus_b, comma_b, backspace_b, backspace_b_2
    global dict_keyboard
    global geo_calc_b

    #  Режим "Маршруты"
    route_b = "{name='m_btnRoutes' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"  # Кнопка Маршруты в главном меню

    # Геодезический калькулятор (левая панель)
    geo_calc_b = "{name='qpb_side_left-route_geodesia' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"  

    # Виртуальная клавиатура прямоугольная
    okButton = "{name='m_qpbOK' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"  # Кнопка ОК на виртуальной клавиатуре
    b_1 = "{name='m_qpb1' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_2 = "{name='m_qpb2' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_3 = "{name='m_qpb3' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_4 = "{name='m_qpb4' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_5 = "{name='m_qpb5' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_6 = "{name='m_qpb6' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_7 = "{name='m_qpb7' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_8 = "{name='m_qpb8' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_9 = "{name='m_qpb9' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    b_0 = "{name='m_qpb0' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"
    comma_b = "{name='m_qpbSep' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"  # Кнопка Запятая
    backspace_b = "{name='m_qpbBack1' type='QPushButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"  # Backspace

    #  Словарь со значениями кнопк в вирт клавиатуре
    dict_keyboard = {"1": b_1, "2": b_2, "3": b_3, "4": b_4, "5": b_5, "6": b_6, "7": b_7, "8": b_8, "9": b_9, "0": b_0,
                     ",": comma_b} 

    # В случае неудачного выполнения теста будет сделан скриншот там, где произошла ошибка
    # Сохраняются на десктопе /home/nper/.squish/Test Results/...
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True

#####################################################################
# Геодезический калькулятор
#####################################################################

def geocalc():
    global OGZ_rb
    global plane_rb
    global result_in_DE

    # Задачи RadioButtons
    OGZ_rb = "{name='qrb_ogz' type='QRadioButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"

    # Фигура земли
    plane_rb = "{name='qrb_plain' type='QRadioButton' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"

    # Чек-бокс "Результат в ДУ"
    result_in_DE = "{name='qchk_resultInDE' type='QCheckBox' visible='1' window=':mainWidget_gui::AnimatedStackedWidget'}"

   
