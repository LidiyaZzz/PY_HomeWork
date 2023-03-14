'''
Задача 2: Найдите сумму цифр трехзначного числа.
    Пример:
    123 -> 6 (1 + 2 + 3)
    100 -> 1 (1 + 0 + 0) |
'''

number = input("Ведите трехзначное число: ")
flag = number.isdigit() and len(number) == 3

while not flag:
    number = input("попробуйте ввести трехзначное число еще раз: ")
    flag = number.isdigit() and len(number) == 3

number = int(number)
print("Вы ввели число: ", number)

result = (number % 10) + int((number % 100) / 10) + int((number % 1000) / 100)
print("Сумма цифр числа: ", number, " равна ", result)