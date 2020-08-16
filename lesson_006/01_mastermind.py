# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все обще
# ние с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

import mastermind_engine as me
from termcolor import cprint, colored

cprint('-----Игра «Быки и коровы»-------', color='yellow')
me.make_number()

number_of_moves = 1

cprint('------------Кто играет?--------\n', color='yellow')
cprint('0)------------>Бот', color='yellow')
cprint('1)------------>Вы\n', color='yellow')

while True:
    flag = input(colored('-------------->', color='magenta'))
    if flag not in {'0', '1'}:
        cprint('0)------------>Бот', color='yellow')
        cprint('1------------->Вы', color='yellow')
    else:
        cprint('\n------------START---------------', color='yellow')
        break

if flag == '1':
    while True:
        print()
        number_user = input(
            colored('Введите четырехзначное число c неповторяющимися цифрами!\n\t\t---->', color='magenta'))

        cprint('Ход {}'.format(number_of_moves), color='green')
        if me.checking_number(number_user):
            number_of_moves += 1
        me.game_over(number_user)

elif flag == '0':

    from bot_playing import maybe_the_right_number

    while True:
        number_bot = maybe_the_right_number()

        cprint('Ход {}'.format(number_of_moves), color='green')

        if me.checking_number(number_bot):
            number_of_moves += 1
        me.game_over(number_bot)


else:
    print('Eror!! flag = ', flag)

hasattr()
