'''
    Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
    и возводит число А в целую степень B с помощью рекурсии.

        *Пример:*
        A = 3; B = 5 -> 243 (3⁵)
        A = 2; B = 3 -> 8
'''

import random

def getNumber(str):
    number = input(str)
    flag = number.isdigit()

    while not flag:
        number = input("вы ввели не число, попробуйте еще раз: ")
        flag = number.isdigit()

    return number

numberA = int(getNumber("Введите число А: "))
numberB = int(getNumber("Введите число В: "))

def power(num, pow):
    if num == 0 and pow <= 0:
          print("Невозможно возвести 0 в степень меньше 1")
    if num == 1 or pow == 0:
        return num
    if pow > 1:
        return num * power(num, pow - 1)
    if pow < 1:
        return 1 / num * power(num, ++pow)
    return num

print(f'результат возведения числа {numberA} в степень {numberB}: {power(numberA, numberB)}')

