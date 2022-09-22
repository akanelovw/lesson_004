# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
colors = {"Красный": sd.COLOR_RED,
          "Оранжевый": sd.COLOR_ORANGE,
          "Жёлтый": sd.COLOR_YELLOW,
          "Тёмно-зелёный": sd.COLOR_DARK_GREEN,
          "Берюзовый": sd.COLOR_CYAN,
          "Синий": sd.COLOR_BLUE,
          "Фиолетовый": sd.COLOR_PURPLE}


point_0 = sd.get_point(300, 300)
point_1 = sd.get_point(150, 300)
point_2 = sd.get_point(150, 150)
point_3 = sd.get_point(300, 150)

user_input = input("Введите цвет: ")
for color, color_code in colors.items():
    if user_input == color:
        break
    elif user_input not in colors:
        print("Введён некорректный цвет")
        break
    elif user_input != color:
        continue


def triangle_func(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color_code)
    next_angle = angle + 120
    if next_angle > 240:
        return
    triangle_func(point=v1.end_point, angle=next_angle, length=length)


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color_code)
    next_angle = angle + 90
    if next_angle > 270:
        return
    square(point=v1.end_point, angle=next_angle, length=length)


def five_angles(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color_code)
    next_angle = angle + 72
    if next_angle > 288:
        return
    five_angles(point=v1.end_point, angle=next_angle, length=length)


def six_angles(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color_code)
    next_angle = angle + 60
    if next_angle > 320:
        return
    six_angles(point=v1.end_point, angle=next_angle, length=length)

print("Из предложенных фигур выберите нужную: ",
      "1 - Треугольник",
      "2 - Квадрат",
      "3 - Пятиугольник",
      "4 - Шестиугольник")
user_input_2 = int(input("Введите номер фигуры: "))
if user_input_2 == 1:
    triangle_func(point=point_0, angle=0, length=100)
elif user_input_2 == 2:
    square(point=point_0, angle=0, length=100)
elif user_input_2 == 3:
    five_angles(point=point_0, angle=0, length=75)
elif user_input_2 == 4:
    six_angles(point=point_0, angle=0, length=75)
else:
    print("Введён некорректный номер")

sd.pause()
