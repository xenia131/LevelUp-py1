contacts = {"Вася": 123, "Петя": 223}

while True:
    command = input()
    if command == "exit":
        break
    elif command == "get_contact":
        name = input("Введите имя абонента: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Такого контакта не существует")
    elif command == "add_contact":
        contacts[input()] = int(input())
    else:
        print("Command dont recognized")