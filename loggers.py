def add_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    contact_data = f"Фамилия: {last_name}\nИмя: {first_name}\nОтчество: {middle_name}\nНомер телефона: {phone_number}"

    contact_filename = f"{last_name}_{first_name}_{middle_name}.txt"
    with open(contact_filename, 'w') as file:
        file.write(contact_data)