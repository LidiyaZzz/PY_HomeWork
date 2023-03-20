'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5

'''

import random
count = 0
def getNumber(str):
    number = input(str)
    flag = number.isdigit()

    while not flag:
        number = input("вы ввели не число, попробуйте еще раз: ")
        flag = number.isdigit()

    return number

number = int(getNumber("Введите количество элементов в массиве: "))
value = int(getNumber("Введите значение: "))

numbersList = [i for i in range(0, number)]

if value >= len(numbersList):
    print(f'к значению {value} в массиве {numbersList} самый близкий по величине элемент - {numbersList[-1]}')
else:
    for i in range(0, len(numbersList)):
        if value == numbersList[i]:
            print(f'к значению {value} в массиве {numbersList} самый близкий по величине элемент - {numbersList[i]}')



