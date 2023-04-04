'''
    Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
    Выдать без повторений в порядке возрастания все те числа,
    которые встречаются в обоих наборах.
    Пользователь вводит 2 числа.
    n - кол-во элементов первого множества.
    m - кол-во элементов второго множества.
    Затем пользователь вводит сами элементы множеств.
'''

import random

def getNumber(str):
    number = input(str)
    flag = number.isdigit()

    while not flag:
        number = input("вы ввели не число, попробуйте еще раз: ")
        flag = number.isdigit()

    return number

n = int(getNumber("Введите количество элементов первого множества: "))
m = int(getNumber("Введите количество элементов второго множества: "))

numbersList1 = list()
numbersList2 = list()

for i in range(0, n):
    k = int(getNumber(f"Введите {i} элемент первого множества: "))
    numbersList1.append(k)

for i in range(0, m):
    k = int(getNumber(f"Введите {i} элемент второго множества: "))
    numbersList2.append(k)

resultList = list(set(numbersList1).union(set(numbersList2)))

print(f' массив 1: {numbersList1}')
print(f' массив 2: {numbersList2}')
print(f'числа, которые встречаются в обоих множествах: {resultList}')