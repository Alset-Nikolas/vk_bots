# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class ParsTxtFileGenerate:

    def __init__(self, txt_name_file):
        self.txt_name_file = txt_name_file
        self.data = []

    def parsing_line(self, line):
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        hour = int(line[12:14])
        minute = int(line[15:17])
        value = line[-4:-1]
        return [year, month, day, hour, minute], value

    def read_the_file(self):

        with open(self.txt_name_file, 'r', encoding='cp1251') as file:
            count = 0
            for line in file:
                pars, value = self.parsing_line(line)
                if value == ' OK':
                    continue
                else:
                    self.data.append(pars)

    def generate(self):
        x = 0
        while x != len(self.data):
            yield ('{}-{:02d}-{:02d} {:02d}:{:02d} {}\n'.format(*self.data[x], self.data.count(self.data[x])))
            x += self.data.count(self.data[x])

    def __iter__(self):
        self.i = -1
        self.count_line = 0
        self.early_line = None
        return self

    def __next__(self):
        self.i += 1
        while 1:
            if self.i < len(self.data):
                line = self.data[self.i]

                if self.early_line is None:
                    self.early_line = line
                elif self.early_line == line:
                    self.count_line += 1
                elif self.early_line != line:
                    return(
                        '{}-{:02d}-{:02d} {:02d}:{:02d} {}\n'.format(*line, self.count_line))
                    self.count_line = 1
                    self.early_line = line
                if self.count_line == len(self.data) - 1:
                    return (
                        '{}-{:02d}-{:02d} {:02d}:{:02d} {}\n'.format(*line, self.count_line))
                self.i += 1
        else:
            raise StopIteration


A = ParsTxtFileGenerate(txt_name_file='events.txt')
A.read_the_file()
print('----Генератор--------')
for line in A.generate():
    print(line, end='')


A = ParsTxtFileGenerate(txt_name_file='events.txt')
A.read_the_file()
print('------Итератор-------')
for line in A:
    print(line, end='')