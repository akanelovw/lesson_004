# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:

point_0 = sd.get_point(300, 300)
point_1 = sd.get_point(150, 300)
point_2 = sd.get_point(150, 150)
point_3 = sd.get_point(300, 150)


# def triangle(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw(color=sd.COLOR_RED)
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw(color=sd.COLOR_RED)
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v3.draw(color=sd.COLOR_RED)
#
#
# triangle(point=point_0, angle=0, length=100)


def triangle_func(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_RED)
    next_angle = angle + 120
    if next_angle > 240:
        return
    triangle_func(point=v1.end_point, angle=next_angle, length=length)


triangle_func(point=point_0, angle=0, length=100)


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_RED)
    next_angle = angle + 90
    if next_angle > 270:
        return
    square(point=v1.end_point, angle=next_angle, length=length)


square(point=point_1, angle=0, length=100)


def five_angles(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_RED)
    next_angle = angle + 72
    if next_angle > 288:
        return
    five_angles(point=v1.end_point, angle=next_angle, length=length)


five_angles(point=point_2, angle=0, length=75)


def six_angles(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_RED)
    next_angle = angle + 60
    if next_angle > 320:
        return
    six_angles(point=v1.end_point, angle=next_angle, length=length)


six_angles(point=point_3, angle=0, length=75)

# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
