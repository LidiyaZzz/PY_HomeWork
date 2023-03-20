'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

    Пример:
    5
        1 2 3 4 5
        3
        -> 1
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
value = int(getNumber("Введите значение элемента от 1 до 5: "))

numbersList = [random.randint(0, 5) for i in range(0, number)]
for i in range(0, len(numbersList)):
    if numbersList[i] == value:
        count += 1

print(f' в массиве {numbersList} значение {value} встречается {count} раз')
