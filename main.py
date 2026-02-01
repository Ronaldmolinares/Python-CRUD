clients = [
    {
        "name": "Pablo",
        "company": "Google",
        "email": "pablo@google.com",
        "position": "Software Engineer",
    },
    {
        "name": "Ricardo",
        "company": "Facebook",
        "email": "ricardo@facebook.com",
        "position": "Data Scientist",
    },
    {
        "name": "Ana",
        "company": "Amazon",
        "email": "ana@amazon.com",
        "position": "DevOps Engineer",
    },
]


def create_client(client: dict):
    for existing_client in clients:
        if existing_client["name"] == client["name"]:
            print(f"Client {client['name']} already exists.")
            return
    clients.append(client)


def list_clients():
    print("UID | NAME | COMPANY | EMAIL | POSITION" + "\n" + "-" * 50)
    for idx, client in enumerate(clients, 1):
        print(
            "{uid} | {name} | {company} | {email} | {position}".format(
                uid=idx,
                name=client["name"],
                company=client["company"],
                email=client["email"],
                position=client["position"],
            )
        )


def message_client_not_found(client_name):
    print(f"Error: Client {client_name} not found")


def update_client(client_name):
    for client in clients:
        if client["name"] == client_name:
            print("Press Enter to keep current value or type new value:")
            client["name"] = _get_client_field_or_default("name", client["name"])
            client["company"] = _get_client_field_or_default(
                "company", client["company"]
            )
            client["email"] = _get_client_field_or_default("email", client["email"])
            client["position"] = _get_client_field_or_default(
                "position", client["position"]
            )
            print(f"Client {client_name} updated successfully.")
            return
    message_client_not_found(client_name)


def delete_client(client_name):
    for idx, client in enumerate(clients):
        if client["name"] == client_name:
            clients.pop(idx)
            print(f"Client {client_name} deleted successfully.")
            return
    message_client_not_found(client_name)


def search_client(client_name):
    for client in clients:
        if client["name"] == client_name:
            print("Client found:")
            print(f"  Name: {client['name']}")
            print(f"  Company: {client['company']}")
            print(f"  Email: {client['email']}")
            print(f"  Position: {client['position']}")
            return
    message_client_not_found(client_name)


def _print_welcome():
    print("\n" + ":" * 15 + " WELCOME TO SAM VENTAS " + ":" * 15)
    print("What would you like to do today? ")
    print("[C]reate client")
    print("[L]ist clients")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")
    print("[0] Exit")


def _get_client_field(field_name):
    field_value = str(input(f"Client {field_name}: "))
    while not field_value.strip():
        print(f"The client {field_name} cannot be empty")
        field_value = str(input(f"Client {field_name}: "))

    return field_value.title()


def _get_client_field_or_default(field_name, current_value):
    field_value = input(f"Client {field_name} [{current_value}]: ").strip()
    if field_value:
        return field_value.title()
    return current_value


# def fibonacci(max):
#     a, b = 0, 1
#     while a < max:
#         yield a
#         a, b = b, a + b


if __name__ == "__main__":
    while True:
        _print_welcome()
        command = input()
        match command.lower():
            case "c":
                client = {
                    "name": _get_client_field("name"),
                    "company": _get_client_field("company"),
                    "email": _get_client_field("email"),
                    "position": _get_client_field("position"),
                }
                create_client(client)
                print(f"Client {client['name']} created successfully.")

            case "l":
                list_clients()

            case "u":
                client_name = _get_client_field("name")
                update_client(client_name)

            case "d":
                client_name = _get_client_field("name")
                delete_client(client_name)

            case "s":
                client_name = _get_client_field("name")
                search_client(client_name)

            # case "f":
            #     max = int(input("Enter the maximum number for Fibonacci sequence: "))
            #     print(f"Fibonacci sequence up to {max}:")
            #     for number in fibonacci(max):
            #         print(number, end=", ")
            #     print()

            case "0":
                print("Exiting...")
                break

            case _:
                print("Invalid Option. Try again")
