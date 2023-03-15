'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа
X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.

'''

import math
def getNumber(str):
    number = input(str)
    flag = number.isdigit()

    while not flag:
        number = input("вы ввели не число, попробуйте еще раз: ")
        flag = number.isdigit()

    return number

s = int(getNumber("Введите сумму загаданных чисел: "))
p = int(getNumber("Введите произведение загаданных чисел: "))

d = s * s - 4 * p

if d < 0:
   print("Так не бывает!")
else:
    sd = math.sqrt(d)
    numY = (s + sd) / 2
    numX = s - numY

print(numY)
print(numX)