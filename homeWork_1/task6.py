'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

    Пример:
    385916 -> yes
    123456 -> no
'''

number = input("Введите номер билета: ")
flag = number.isdigit() and len(number) == 6

while not flag:
    number = input("попробуйте ввести номер билета еще раз: ")
    flag = number.isdigit() and len(number) == 6

resultLeft = 0
resultRight = 0

for i in range(3):
    resultLeft += int(number[i])
    resultRight += int(number[i+3])

number = int(number)
print("Вы ввели число: ", number)

print("Сумма цифр справа: ", resultLeft, "Сумма цифр слева: ", resultRight)

if resultLeft == resultRight:
    print("Да! Вы счастливчик!")
else:
    print("Этот билет не счастливый. Повезет в другой раз!")