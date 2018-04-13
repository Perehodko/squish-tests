'''
Тест позволяет проверить работу функции, сымитировать набор данных на виртуальной клавиатуре пользователем.
Данные берутся из внешенго файла -- data_OGZ_plane.tsv.
'''
#  Инициализация полей ввода
x_field = "{container=':mainWidget.qstw_mode_QStackedWidget' name='qle_ogz_x' type='QLineEdit' visible='1'}"
y_field = "{container=':mainWidget.qstw_mode_QStackedWidget' name='qle_ogz_y' type='QLineEdit' visible='1'}"
x1_field = "{container=':mainWidget.qstw_mode_QStackedWidget' name='qle_ogz_x_2' type='QLineEdit' visible='1'}"
y1_field = "{container=':mainWidget.qstw_mode_QStackedWidget' name='qle_ogz_y_2' type='QLineEdit' visible='1'}"

def init():
    source(findFile("scripts", "script_file_squish.py"))
    all()
    
point1 = 143
point2 = 12
def cliking(x, x_field, point1, point2):
    value_X = []  # Создаю пустой список
    for i in x:
        value_X.append (i)  # Для текущей итерации значение поля X из таблицы преобразую в список
        mouseClick(waitForObject(x_field), point1, point2, 0, Qt.LeftButton) #  Ставлю курсор на нужное поле
    for key in value_X:  # По ключу обращаюсь к вирт.клавиатуре
        clickButton((dict_keyboard[key]))  # Набираю значение из поля Х
        snooze(0.2) #  Задержка, иначе не успевает нажимать на клавиши клавы
        
def main():
    num = 0 
    startApplication("ArmkApplication")
    clickButton(waitForObject(route_b)) 
    clickButton(waitForObject(geo_calc_b)) 
    clickButton(waitForObject(OGZ_rb)) 
    
    #  Заполнение режима ПГЗ-Сфера
    for record in testData.dataset("data_OGZ_plane.tsv"):
        x = testData.field(record, "X")
        y = testData.field(record, "Y")
        x1 = testData.field(record, "X1")
        y1 = testData.field(record, "Y1")
        result_S_n = testData.field(record, "result_S")
        result_A_n = testData.field(record, "result_A")
        
        x11_point = 143 #  Координаты (x; y) наведения курсора
        x12_point = 12
        
        y11_point = 142
        y12_point = 15
        
        x21_point = 152
        x22_point = 17
        
        y21_point = 152
        y22_point = 13
        
        #  Счетчик выполненных тестов
        num += 1
        test.log("Тест №", str(num))

        cliking(x, x_field, x11_point, x12_point) 
        cliking(y, y_field, y11_point, y12_point) 
        cliking(x1, x1_field, x21_point, x22_point)
        cliking(y1, y1_field, y21_point, y22_point) 

        #  Сравнение выводимго результата с ожидаемым из файла data_OGZ_plane.tsv. Поля -- result_S_n, result_A_n
        test.compare(str(waitForObjectExists(":qstw_mode.qle_ogz_s_QLineEdit").displayText), result_S_n)
        test.compare(str(waitForObjectExists(":qstw_mode.qle_ogz_a_QLineEdit").displayText), result_A_n)
    
    #  Чек-бокс "Результат в ДУ" должен быть неактивным: enabled = False
    test.compare(waitForObjectExists(":mainWidget.qchk_resultInDE_QCheckBox").enabled, False)
    test.log("Всего тестов выполнено", str(num))
