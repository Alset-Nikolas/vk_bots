# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
print('---------------------------------------------Часть 1-----------------------------------------------')

'''
def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

'''


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.i = -1
        self.prime_numbers = []

        for number in range(2, self.n + 1):  # TODO цикла здесь быть не должно
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.prime_numbers.append(number)

    # TODO я не хотел в __init__ ставить цикл, пытался в enter, но не работает! Почему?
    # TODO потому, что цикл должен быть в __next__
    # def __enter__(self):
    #    for number in range(2, self.n + 1):
    #        for prime in self.prime_numbers:
    #            if number % prime == 0:
    #                break
    #        else:
    #            self.prime_numbers.append(number)
    #

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):  # TODO цикл должен быть здесь
        self.i += 1
        if self.i < len(self.prime_numbers):  # TODO ограничение должно быть по кол-ву запрашиваемых чисел n
            return self.prime_numbers[self.i]
        else:
            raise StopIteration


prime_number_iterator = PrimeNumbers(n=100)  # TODO по заданию требуется до 10000
# for number in prime_number_iterator:
#     print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик
print('-------------------------------------------Часть 2-------------------------------------------------')


def prime_numbers_generator(n):
    sito = [0] * n
    for i in range(n):
        if i == 0 or i == 1:
            sito[i] = -1
        elif sito[i] == 0:
            sito[i] = 1
            yield i
            k = 2
            while i * k < n:
                sito[i * k] = -1
                k += 1


prime_numbers_generator(n=100)

# for number in prime_numbers_generator(n=10000):
#     print(number)

print('-----------------------------------------------Часть 3_1---------------------------------------------')


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
class PrimeNumbersAndHappy(PrimeNumbers):  # TODO подход к решению через класс здесь не нужен

    def __init__(self, n):
        super().__init__(n)
        self.prime_happy_numbers = []

    def function_filter_happy(self, number):
        number_str = str(number)
        if len(number_str) % 2 == 0:
            left = number_str[:len(number_str) // 2]
            right = number_str[len(number_str) // 2:]
        else:
            left = number_str[:len(number_str) // 2]
            right = number_str[len(number_str) // 2 + 1:]
        a = 0
        b = 0
        for iter in left:
            a += int(iter)
        for iter in right:
            b += int(iter)
        if a == b:
            return True
        return False
    def filter(self):
        for number in self.prime_numbers:
            if self.function_filter_happy(number):
                self.prime_happy_numbers.append(number)

    # TODO концепция функции-фильтра применена не верна
    #  свою писать не нужно, нужно использовать готовую из builtins.py
    #  Пример: for number in filter(is_palindrome_number, prime_numbers_generator(n=20000)):

    def __iter__(self):
        super().__iter__()
        self.filter()

    def __next__(self):
        self.i += 1
        if self.i < len(self.prime_happy_numbers):
            return self.prime_happy_numbers[self.i]
        else:
            raise StopIteration


A = PrimeNumbersAndHappy(n=1000)
# for number in A:
#     print(number)


# TODO оформить код по PEP8


print('-----------------------------------------------Часть 3_2---------------------------------------------')
class PrimeNumbersAndPolindrom(PrimeNumbers):

    def polindrom(self, number):
        number_str = str(number)
        flag = True
        for i in range(len(number_str)):
            if number_str[i] != number_str[-(i + 1)]:
                return False
            return True

    def __next__(self):
        self.i += 1
        if self.i < len(self.prime_numbers):
            if self.polindrom(self.prime_numbers[self.i]):
                return self.prime_numbers[self.i]
            else:
                self.__next__()
        else:
            raise StopIteration


A = PrimeNumbersAndPolindrom(n=1000)
for number in A:
    print(number)
