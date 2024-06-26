def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact added."
    return f"{name} not exist."

def show_contact(name, contacts):
    if name in contacts:
        return f"{name} phone {contacts[name]}."
    return f"{name} not exist."

def all_contact(contacts):
    some_str=""
    for name, phone in contacts.items():
        some_str+=f"{name} = {phone}\n"
    return some_str


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args[0], contacts))
        elif command == "all":
            print(all_contact(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


