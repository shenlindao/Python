import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for contact in data:
            print(contact, end='')
        input('\nНажмите любую клавишу для продолжения')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a', encoding='utf-8') as file:
        res = ''
        res += input('Введите фамилию: ') + ' '
        res += input('Введите имя: ') + ' '
        res += input('Введите телефон: ')
        file.write('\n' + res)
    input('Контакт успешно добавлен! Нажмите любую клавишу для возврата')

def search_contact(file_name):
    os.system('CLS')
    target = input('Введите запрос для поиска: ')
    with open(file_name, 'r', encoding='utf-8') as file:
        contacts = file.readlines()
        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else:
            print('Такого контакта не существует')
    input('Нажмите любую клавишу для продолжения')

def drawing():
    print('1 - Показать все контакты')
    print('2 - Добавить контакт')
    print('3 - Найти контакт')
    print('4 - Удалить контакт')
    print('5 - Выход')

def delete_contact(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as data:
        contact = data.read()
        print(contact)
    print('')
    delete_index = int(input("Введите номер строки для удаления: ")) - 1
    lines = contact.split("\n")
    delete_lines = lines[delete_index]
    lines.pop(delete_index)
    print(f"Удалена запись: {delete_lines}\n")
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input('Введите номер от 1 до 4: '))
        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            delete_contact(file_name)
        elif user_choice == 5:
            print('Хорошего дня!')
            return