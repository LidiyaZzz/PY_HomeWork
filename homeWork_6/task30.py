'''
    Задача 30:  Заполните массив элементами арифметической прогрессии. Её
    первый элемент, разность и количество элементов нужно ввести с клавиатуры.
    Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
    Каждое число вводится с новой строки.
'''

def getNumber(str):
    number = input(str)
    flag = number.isdigit()

    while not flag:
        number = input("вы ввели не число, попробуйте еще раз: ")
        flag = number.isdigit()

    return number

el = int(getNumber("Введите первый элемент: "))
d = int(getNumber("Введите разность элементов: "))
n = int(getNumber("Введите количество элементов: "))

elementsList = list()

for i in range(0, n):
    k = el + i * d
    elementsList.append(k)

print(f'массив элементами арифметической прогрессии: {elementsList}')