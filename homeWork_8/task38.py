'''
    Задача 38:
    Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
    Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

    Дополнить телефонный справочник возможностью изменения и удаления данных.
    Пользователь также может ввести имя или фамилию,
    и Вы должны реализовать функционал для изменения и удаления данных

    1. Программа должна выводить данные
    2. Программа должна сохранять данные в текстовом файле
    3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
    4. Использование функций. Ваша программа не должна быть линейной

    def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")
    choice = int(input())
    return choice
'''
import shutil

def readCsv(filename='phonebook.csv') -> list:
    with open(filename, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            data.append(line.strip('\n').split(','))
    return data


def displayAllRecords():
    data = readCsv()
    for row in data:
        print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def findLastName():
    last_name = input('Введите фамилию: ')
    data = readCsv()
    for row in data:
        if row[0] == last_name:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def findPhoneNumber():
    phone = input('Введите номер телефона: ')
    data = readCsv()
    for row in data:
        if row[2] == phone:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def addData(filename='phonebook.csv'):
    with open(filename, 'a', encoding='utf-8') as file:
        info = input('Введите данные абонента (фамилия, имя, номер, комментарий - через запятую): ').split(', ')
        file.write('\n' + ','.join(info) + '\n')
        print('Данные записаны.')


def delUserInfo(filename='phonebook.csv'):
    info = input('Введите данные абонента (фамилия, имя, номер телефона - через запятую): ').split(', ')
    data = readCsv()
    flag = True

    for row in data:
        if row[0] == info[0] and row[1] == info[1] and row[2] == info[2]:
            print('Данные найдены.')
            data.remove(row)
            flag = False
            break

    if flag:
        print('Данные не найдены.')

    with open(filename, 'w', encoding='utf-8') as file:
        for row in data:
            info = ''
            for i in range(len(row)):
                if i == 0:
                    info += row[i]
                else:
                    info += ',' + row[i]
            file.write(''.join(info) + '\n')
        if flag == False:
            print('Данные удалены.')


def changeUserInfo(filename='phonebook.csv'):
    info = input('Введите данные абонента (фамилия, имя, номер телефона - через запятую): ').split(', ')
    data = readCsv()
    flag = True

    for row in data:
        if row[0] == info[0] and row[1] == info[1] and row[2] == info[2]:
            newInfo = input('Введите измененные данные через запятую: ').split(', ')
            data.remove(row)
            data.append(newInfo)
            flag = False
            break

    if flag:
        print('Данные не найдены.')

    with open(filename, 'w', encoding='utf-8') as file:
        for row in data:
            info = ''
            for i in range(len(row)):
                if i == 0:
                    info += row[i]
                else:
                    info += ',' + row[i]
            file.write(''.join(info) + '\n')
        if flag == False:
            print('Данные изменены.')


def saveFileTxt():
    with open(input('Введите имя файла: ')+'.txt', 'w', encoding='utf-8') as newFile:
        data = readCsv()
        for row in data:
            info = ''
            for i in range(len(row)):
                if i == 0:
                    info += row[i]
                else:
                    info += ',' + row[i]
            newFile.write(''.join(info) + '\n')
        print('Файл сохранен. Чтобы увидеть файл завершите работу (нажмите 8)')


number = 0
while number != '8':
    print('Введите число для операции со справочником:')
    print('1 - вывести весь справочник;\n2 - найти абонента по фамилии;\n'
          '3 - найти абонента по номеру телефона;\n4 - ввести данные нового абонента;\n'
          '5 - сохранить справочник в текстовом формате;\n'
          '6 - удалить данные.\n7 - заменить данные.\n'
          '8 - завершить работу.\n')

    number = input()

    if number == '1':
        displayAllRecords()

    elif number == '2':
        findLastName()

    elif number == '3':
        findPhoneNumber()

    elif number == '4':
        addData()

    elif number == '5':
        saveFileTxt()

    elif number == '6':
        delUserInfo()

    elif number == '7':
        changeUserInfo()

else:
    print('Работа завершена.')


