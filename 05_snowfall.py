# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def snowflake():
    y = 600
    x = sd.random_number(0, 1200)
    length = sd.random_number(35, 50)
    factor_a = sd.random_number(5, 10) / 10
    while True:
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length, factor_a=factor_a, color=sd.COLOR_WHITE)
        sd.sleep(0.1)
        y -= 30
        x += sd.random_number(-10, 10)
        sd.snowflake(center=point, length=length, factor_a=factor_a, color=sd.background_color)
        if sd.user_want_exit():
            break
        elif y < 0:
            sd.snowflake(center=point, length=length, factor_a=factor_a)
            break


for _ in range(100):
    snowflake()
    if sd.user_want_exit():
        break


# while True:
#     sd.clear_screen()
#     pass
#     pass
#     pass
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


