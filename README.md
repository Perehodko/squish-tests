# tests
Тест позволяет проверить работу функции, сымитировать набор данных на виртуальной клавиатуре пользователем.
Пример теста на Python. Используется Sqish.
Во внешнем файле (data_OGZ_plane.tsv) фикисруются наборы входных данных (x1, x2, y1, y2) и ожидаемый результат (S и A).

1. Запускаем приложение.
2. Осуществляем переход в нужный режим.
3. Вводим данные (x1, x2, y1, y2).
4. Сравниваем результат расчета в форме с ожидаемым результатом из файла.
5. Чек-бокс "Результат в ДУ" должен быть неактивным: enabled = False
