'''
    Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
    Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
    Вам стоит написать программу.
    Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
    в каждой фразе стихотворения одинаковое.
    Фраза может состоять из одного слова, если во фразе несколько слов,
    то они разделяются дефисами.
    Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
    В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

    Пример:
        Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
        Вывод: Парам пам-пам
'''

verse = input("напишите кричалку: слова во фразе разделите дефисами. Фразы отделите друг от друга пробелами: ")
strBase = verse.split(' ')


def success():
    print('Парам пам-пам! С ритмом все в порядке!')


def failed():
    print('Пам парам. С ритмом все не в порядке!')


def count(word):
    vowels = 0
    for i in word:
        letter = i.lower()
        if letter == "а" or letter == "о" or \
                letter == "у" or letter == "и" or \
                letter == "ы" or letter == "ю" or \
                letter == "я" or letter == "е":
            vowels += 1
    return vowels


if len(strBase) == 1:
    success()
else:
    for i in range(1, len(strBase)):
        if count(strBase[0]) != count(strBase[i]):
            failed()
            break
        if i == len(strBase) - 1:
            success()
            break



