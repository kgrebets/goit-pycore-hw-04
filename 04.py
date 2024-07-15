def parse_input(cmd_string):
    cmd, *args = cmd_string.split()
    cmd = cmd.strip().lower()
    return (cmd, args)

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Not enough arguments. Usage: add [name] [phone number]"
   
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Not enough arguments. Usage: change [name] [new phone number]"
   
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."
    
def delete_contact(args, contacts):
    if len(args) != 1:
        return "Error: Not enough arguments. Usage: delete [name]"
   
    name = args[0]
    if name in contacts:
        contacts.pop(name)
        return "Contact removed."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Not enough arguments. Usage: phone [name]"
    
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

def show_all(contacts):
    if len(contacts) == 0:
        return "No contacts found."

    contact_strings = [f"{name}: {phone}" for (name, phone) in contacts.items()]
    result = "\n".join(contact_strings)
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        cmd_string = input("Enter a command: ")
        cmd, args = parse_input(cmd_string)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, contacts))
        elif cmd == "change":
            print(change_contact(args, contacts))
        elif cmd == "delete":
            print(delete_contact(args, contacts))
        elif cmd == "phone":
            print(show_phone(args, contacts))
        elif cmd == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

main()
