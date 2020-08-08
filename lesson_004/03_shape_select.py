# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

color = {
    0:
        {'Красный': sd.COLOR_RED},
    1:
        {'Оранжевый': sd.COLOR_ORANGE},
    2:
        {'Желтый': sd.COLOR_YELLOW},
    3:
        {'Зеленый': sd.COLOR_GREEN},
    4:
        {'Голубой': sd.COLOR_CYAN},
    5:
        {'Синий': sd.COLOR_BLUE},
    6:
        {'Фиолетовый': sd.COLOR_PURPLE},
}

figures = ['Трекульник', 'Квадрат', 'Пятиугольник', 'Шестиугольник']


def n_corners(number_of_sides, start_point=sd.Point(350, 250), angle=45, length=100, color=sd.COLOR_YELLOW):
    length = length * 6 / number_of_sides
    start_point_0 = start_point
    delta = round(360 / number_of_sides)
    for angle_alfa in range(angle, 360 + angle, delta):
        side = sd.Vector(start_point=start_point, direction=angle_alfa, length=length, width=3)
        side.draw(color=color)
        start_point = side.end_point
    else:
        end_point = start_point
        point_list = [start_point_0, end_point]
        sd.lines(point_list, color=color, closed=False, width=3)


def choose_color(color):
    print()
    print('\t----------------')
    print('\tВозможные цвета:')
    print('\t----------------')
    print()
    len_str = len('Красный 	 0')

    for i in color:
        key = list(color[i].keys())[0]
        print('\t', key, ' ' * (len_str - len(key)), i)

    while True:
        print()
        number_color = input('Введите желаемый цвет > ')
        try:
            number_color = int(number_color)
        except:
            print('Число!')
        if isinstance(number_color, int) and 0 <= number_color <= 6:
            print()
            print('\t  Хороший выбор!')
            print()
            break
        else:
            print('Вы ввели не корректный номер!')
    return number_color


def choose_figure(figures):
    print('\t-----------------')
    print('\tВозможные фигуры:')
    print('\t-----------------')

    len_str = len('Трекульник 	 0')
    for i, figure in enumerate(figures):
        print('\t', figure, ' ' * (len_str - len(figure)), i)

    while True:
        print()
        number_figure = input('Введите желаемую фигуру > ')
        try:
            number_figure = int(number_figure)
        except:
            print('Число!')
        if isinstance(number_figure, int) and 0 <= number_figure <= 3:
            print()
            print('\t  Хороший выбор!')
            print()
            break
        else:
            print('Вы ввели не корректный номер!')
    return number_figure


number_color = choose_color(color)
number_figure = choose_figure(figures)


def draw(number_color, number_figure, color):
    n_corners(number_of_sides=number_figure + 3, start_point=sd.Point(300, 300),
              color=list(color[number_color].values())[0])


draw(number_color, number_figure, color)

sd.pause()