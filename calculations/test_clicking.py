x_field = "{container=':mainWidget.qstw_mode_QStackedWidget' name='qle_ogz_x' type='QLineEdit' visible='1'}"
y_field = "{container=':mainWidget.qstw_mode_QStackedWidget' name='qle_ogz_y' type='QLineEdit' visible='1'}"
x1_field = "{container=':mainWidget.qstw_mode_QStackedWidget' name='qle_ogz_x_2' type='QLineEdit' visible='1'}"
y1_field = "{container=':mainWidget.qstw_mode_QStackedWidget' name='qle_ogz_y_2' type='QLineEdit' visible='1'}"

def init():
    source(findFile("scripts", "script_file_squish.py"))
    all()
    initial_PTS()
    geocalc()
    routes()
    
def main():
    num = 0 
      
    startApplication("ArmkApplication")
    clickButton(waitForObject(route_b)) 
    snooze(3)
    clickButton(waitForObject(geo_calc_b)) 
    clickButton(waitForObject(OGZ_rb)) 
    #Заполнение режима ПГЗ-Сфера
    for record in testData.dataset("data_OGZ_plane.tsv"):
        x = testData.field(record, "X")
        y = testData.field(record, "Y")
        x1 = testData.field(record, "X1")
        y1 = testData.field(record, "Y1")
        result_S_n = testData.field(record, "result_S")
        result_A_n = testData.field(record, "result_A")
        
       #Счетчик выполненных тестов
        num += 1
        test.log("Тест №", str(num))

        value_X = [] #Создаю пустой список
        for i in x:
            value_X.append(i) #Для текущей итерации значение поля X из таблицы преобразую в список
        mouseClick(waitForObject(x_field), 143, 12, 0, Qt.LeftButton) #Ставлю курсор на нужное поле
        for key in value_X: #По ключу обращаюсь к вирт.клавиатуре 
            clickButton(waitForObject(dict_keyboard[key]))#Набираю значение из поля Х 
            snooze(0.2) #Задержка, иначе не успевает нажимать на клавиши клавы

        value_Y = []
        for i in y:
            value_Y.append(i) 
        mouseClick(waitForObject(y_field), 142, 15, 0, Qt.LeftButton)
        for key in value_Y:
            clickButton(waitForObject(dict_keyboard[key]))
            snooze(0.2)

        '''#Смена знака у L
        snooze(0.2)
        mouseClick(waitForObject(plus_minus_b))
        snooze(1)'''
        
        value_X1 = []
        for i in x1:
            value_X1.append(i) 
        mouseClick(waitForObject(x1_field), 152, 17, 0, Qt.LeftButton)
        for key in value_X1:
            clickButton(waitForObject(dict_keyboard[key]))
            snooze(0.2) 
     
        value_Y1 = []
        for i in y1:
            value_Y1.append(i) 
        mouseClick(waitForObject(y1_field), 152, 13, 0, Qt.LeftButton)
        for key in value_Y1:
            clickButton(waitForObject(dict_keyboard[key]))
            snooze(0.2) 
            
        test.compare(str(waitForObjectExists(":qstw_mode.qle_ogz_s_QLineEdit").displayText), result_S_n)
        test.compare(str(waitForObjectExists(":qstw_mode.qle_ogz_a_QLineEdit").displayText), result_A_n)
    
    
    #Чек-бокс "Результат в ДУ" должен быть неактивным: enabled = False
    test.compare(waitForObjectExists(":mainWidget.qchk_resultInDE_QCheckBox").enabled, False)

    test.log("Всего тестов выполнено", str(num))
