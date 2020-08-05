# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

percents_change = 3 / 100
months = 9

summa = expenses - educational_grant

while months != 0:
    dif = expenses * (1 + percents_change) - educational_grant
    summa += dif
    months -= 1


else:
    print('Студенту надо попросить', round(summa, 2), 'рублей')

