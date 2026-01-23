clients = "Cliente 1, Cliente 2"


def create_client(client_name):
    global clients

    if client_name not in clients:
        _add_comma()
        clients += client_name
    else:
        print(f"Error: A client with the name already exists: {client_name}")


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ", "


def _print_welcome():
    print(":" * 15 + " WELCOME TO SAM VENTAS " + ":" * 15)
    print("What would you like to do today? ")
    print("[C]reate client")
    print("[D]elete client")


if __name__ == "__main__":
    _print_welcome()
    command = input()
    if command.lower() == "c":
        name = str(input("Name of client: "))
        create_client(name.title())
        list_clients()
    elif command.lower() == "d":
        pass
    else:
        print("Invalid Option. Try again")
