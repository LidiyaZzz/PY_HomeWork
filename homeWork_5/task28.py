'''
    Задача 28: Напишите рекурсивную функцию sum(a, b),
    возвращающую сумму двух целых неотрицательных чисел.
    Из всех арифметических операций допускаются только +1 и -1.
    Также нельзя использовать циклы.

    *Пример:*

    2 2
        4
'''

def getNumber(str):
    number = input(str)
    flag = number.isdigit()

    while not flag:
        number = input("вы ввели не число, попробуйте еще раз: ")
        flag = number.isdigit()

    return number

numberA = int(getNumber("Введите число А: "))
numberB = int(getNumber("Введите число В: "))

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

print(f'результат сложения числа {numberA} с числом {numberB}: {sum(numberA, numberB)}')

