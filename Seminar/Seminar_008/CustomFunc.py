import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for contact in data:
            print(contact, end='')
        input('\nНажмите Enter для продолжения')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a', encoding='utf-8') as file:
        res = ''
        res += input('Введите фамилию: ') + ' '
        res += input('Введите имя: ') + ' '
        res += input('Введите телефон: ')
        file.write('\n' + res)
    input('Контакт успешно добавлен! Нажмите Enter для возврата')

def search_contact(file_name):
    os.system('CLS')
    target = input('Введите запрос для поиска: ')
    with open(file_name, 'r', encoding='utf-8') as file:
        contacts = file.readlines()
        for contact in contacts:
            if target in contact:
                print('')
                print(contact)
                break
        else:
            print('')
            print('Такого контакта не существует')
    input('Нажмите Enter для продолжения')

def delete_contact(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for n, contact in enumerate(data, start=1):
            print(n, '-', contact, end='')
    print('')
    delete_index = int(input("\nВведите номер строки для удаления: ")) - 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact, line in enumerate(data):
            if contact not in [delete_index]:
                file.write(line)

def edit_contact(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for n, contact in enumerate(data, start=1):
            print(n, '-', contact, end='')
    edit_index = int(input("\nВведите номер строки для редактирования: ")) - 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact, line in enumerate(data):
            if contact in [edit_index]:
                res = ''
                res += input('Введите фамилию: ') + ' '
                res += input('Введите имя: ') + ' '
                res += input('Введите телефон: ')
                file.write(res + '\n')
            else:
                file.write(line)
    input('\nНажмите Enter для возврата')

def drawing():
    print('1 - Показать все контакты')
    print('2 - Добавить контакт')
    print('3 - Найти контакт')
    print('4 - Редактировать контакт')
    print('5 - Удалить контакт')
    print('6 - Выход')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input('Введите номер нужной операции от 1 до 6: '))
        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            edit_contact(file_name)
        elif user_choice == 5:
            delete_contact(file_name)
        elif user_choice == 6:
            print('Хорошего дня!')
            return