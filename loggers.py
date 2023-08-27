import os


def add_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    contact_data = f"Фамилия: {last_name}\nИмя: {first_name}\nОтчество: {middle_name}\nНомер телефона: {phone_number}"

    contact_filename = f"{last_name}_{first_name}_{middle_name}.txt"
    with open(contact_filename, 'w') as file:
        file.write(contact_data)


def search_contact():
    search_term = input("Введите фамилию, имя или отчество для поиска: ")

    found_contacts = []
    for filename in os.listdir():
        if filename.endswith(".txt"):
            with open(filename, 'r') as file:
                if search_term.lower() in file.read().lower():
                    found_contacts.append(filename)

    if found_contacts:
        print("Найденные контакты:")
        for contact in found_contacts:
            print(contact)
    else:
        print("Контакты не найдены.")


def correction_contact(contact_filename):
    try:
        with open(contact_filename, 'r') as file:
            contact_data = file.read()
            print("Текущая информация о контакте:\n", contact_data)

        last_name, first_name, middle_name = contact_filename[:-4].split('_')
        new_last_name = input("Введите новую фамилию: ")
        new_first_name = input("Введите новое имя: ")
        new_middle_name = input("Введите новое отчество: ")
        new_phone_number = input("Введите новый номер телефона: ")

        new_contact_data = (
            f"Фамилия: {new_last_name}\n"
            f"Имя: {new_first_name}\n"
            f"Отчество: {new_middle_name}\n"
            f"Номер телефона: {new_phone_number}"
        )

        new_contact_filename = f"{new_last_name}_{new_first_name}_{new_middle_name}.txt"

        if contact_filename != new_contact_filename:
            os.rename(contact_filename, new_contact_filename)

        with open(new_contact_filename, 'w') as file:
            file.write(new_contact_data)
            print("Информация о контакте обновлена.")
    except FileNotFoundError:
        print("Контакт не найден.")


def delete_contact(contact_filename):
    try:
        os.remove(contact_filename)
        print("Контакт успешно удален.")
    except FileNotFoundError:
        print("Контакт не найден.")