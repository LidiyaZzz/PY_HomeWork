'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть

'''
import random

head = 0
tail = 0
coins = ""

number = input("Ведите общее количество монет: ")
flag = number.isdigit()

while not flag:
    number = input("вы ввели не число, попробуйте еще раз: ")
    flag = number.isdigit()

number = int(number)

for i in range(number):
    num = random.randint(0, 1)
    if num == 1:
        head += 1
    if num == 0:
        tail += 1
    if i == 0:
        coins += str(num)
    else:
        coins += ", " + str(num)


if head > tail or head == tail:
    print("На столе лежат монетки: ", coins, "где 1 - герб, а 0 - решка.")
    print("Нужно перевернуть ", tail, "монет, чтобы все были повернуты вверх гербом")
if head < tail:
    print("На столе лежат монетки: ", coins, "где 1 - решка, а 0 - герб.")
    print("Нужно перевернуть ", head, "монет, чтобы все были повернуты вверх решкой")