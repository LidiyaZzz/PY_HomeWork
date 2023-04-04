'''
    Задача 32: Определить индексы элементов массива (списка), значения которых
    принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
    больше заданного максимума)
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
valueMin = int(getNumber("Введите минимальное значение: "))
valueMax = int(getNumber("Введите максимальное значение: "))

numbersList = [random.randint(-10, 15) for i in range(0, number)]
elementsList = list()

for i in range(len(numbersList)):
    if valueMin <= numbersList[i] <= valueMax:
        elementsList.append(i)


print(f'массив {numbersList}')
print(f'индексы элементов, значения которых принадлежат заданному диапазону: {elementsList}')