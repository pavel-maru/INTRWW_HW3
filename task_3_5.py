# 5. Усовершенствовать первую функцию из предыдущего примера.
# Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения,
# вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
# состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.


import os
import random

LINES_COUNT = STRING_SIZE = 10
NUMBER_FIRST_SIZE = 100
NUMBER_IN_STRING_SIZE = 1000


def get_random_string():
    return ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(STRING_SIZE)])


def create_text_file(name):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует')
        return False
    with open(name, 'w', encoding='utf-8') as file:
        numbers = [random.randint(0, NUMBER_FIRST_SIZE) for _ in range(LINES_COUNT)]
        strings = []
        for _ in range(LINES_COUNT):
            if random.randint(0, 10) % 2 == 0:
                strings.append(f'{get_random_string()}{random.randint(0, NUMBER_IN_STRING_SIZE)}')
            else:
                strings.append(f'{get_random_string()}')
        file.writelines([f'{number}\t{text}\n' for number, text in zip(numbers, strings)])
        return file


def print_text_file(desc):
    with open(desc.name, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


descriptor = create_text_file('newfile.txt')
if descriptor:
    print_text_file(descriptor)
