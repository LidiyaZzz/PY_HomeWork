'''
Требуется вывести все целые степени двойки
(т.е. числа вида 2k), не превосходящие числа N.

'''

number = input("Ведите число N: ")
flag = number.isdigit()

while not flag:
    number = input("вы ввели не число, попробуйте еще раз: ")
    flag = number.isdigit()

number = int(number)
result = 0
counter = 1
flag = True

print(f"все целые степени двойки до числа {number}: ", end = " ")
while flag:
    result = 2 ** counter
    counter += 1
    if result < number:
        print(result, end = " ")
    else:
        flag = False

