from loggers import add_contact, search_contact, correction_contact

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить контакт")
        print("2. Поиск контакта")
        print("3. Изменить данные контакта")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            contact_filename = input("Введите имя файла контакта для изменения: ")
            correction_contact(contact_filename)
        elif choice == '4':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()