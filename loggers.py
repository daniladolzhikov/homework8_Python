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