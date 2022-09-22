# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
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


triangle_func(point=point_0, angle=0, length=100)


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color_code)
    next_angle = angle + 90
    if next_angle > 270:
        return
    square(point=v1.end_point, angle=next_angle, length=length)


square(point=point_1, angle=0, length=100)


def five_angles(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color_code)
    next_angle = angle + 72
    if next_angle > 288:
        return
    five_angles(point=v1.end_point, angle=next_angle, length=length)


five_angles(point=point_2, angle=0, length=75)


def six_angles(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color_code)
    next_angle = angle + 60
    if next_angle > 320:
        return
    six_angles(point=v1.end_point, angle=next_angle, length=length)


six_angles(point=point_3, angle=0, length=75)


sd.pause()
