# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных



# r - только чтение файла
# a - дозапись в файл
# w - перезапись файла


phone_book = {}

def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    phone_book[name] = phone
    print(f"Контакт {name} успешно добавлен в справочник.")

def edit_contact():
    name = input("Введите имя контакта, который хотите отредактировать: ")
    if name in phone_book:
        phone = input("Введите новый номер телефона: ")
        phone_book[name] = phone
        print(f"Контакт {name} успешно изменен.")
    else:
        print(f"Контакт {name} не найден в справочнике.")

def delete_contact():
    name = input("Введите имя контакта, который хотите удалить: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} успешно удален.")
    else:
        print(f"Контакт {name} не найден в справочнике.")

def print_contacts():
    if phone_book:
        print("Список контактов:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    else:
        print("Справочник пуст.")

def main():
    while True:
        print("Меню:")
        print("1. Добавить контакт")
        print("2. Редактировать контакт")
        print("3. Удалить контакт")
        print("4. Показать все контакты")
        print("5. Выйти")
        choice = input("Введите номер действия: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print_contacts()
        elif choice == "5":
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == '__main__':
    main()