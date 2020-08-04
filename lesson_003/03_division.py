# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя ни одной из операций деления: ни деления с плавающей точкой /, ни целочисленного деления //
# и взятия остатка %
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
A_const, B_const = a, b

celochislenoe_delenie = 0
while a > 0:
    a -= b
    if a > 0:
        celochislenoe_delenie += 1
    else:
        print('Целочисленное деление ', A_const, ' на ', B_const, ' дает ', celochislenoe_delenie)
        print('Проверка:', A_const // B_const)
