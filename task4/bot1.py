# Task 4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#Greet the bot
def hello_command(args, contacts):
    print("How can I help you?")

# Add a new contact with the given username and phone number
def add_contact(args, contacts):
    print("Please input user contact in format: <name> <phone>")
    user_input = input("> ")  
    args = user_input.strip().split() 
    name, phone = args
    contacts[name] = phone
    print("Contact added.")

# Update the phone number of an existing contact
def change_command(args, contacts):
    print("Please input contact to change in format: <name> <phone>")
    user_input = input("> ")  
    args = user_input.strip().split() 
    if len(args) < 2:
        print("Invalid input. Usage: <name> <phone>")
        return
    
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        print(f"Contact updated: {name} -> {phone}")
    else:
        print(f"Contact '{name}' does not exist. Use 'add' to create it.")

# Show the phone number for the specified contact
def phone_command(args, contacts):
    print("Please input username to display phone in format: <name>")
    user_input = input("> ")  
    args = user_input.strip().split() 
    name = args[0]

    if name in contacts:
         phone = contacts[name]
         print(f"Phonenumber for contact: {phone}")
    else:
         print(f"Contact '{name}' does not exist. Use 'add' to create it.")

# Display all saved contacts with phone numbers
def all_command(args, contacts):
    if not contacts:
        print("No contacts saved yet.")
        return
    
    print("All saved contacts:")
    for name, phone in contacts.items():
        print(f" {name}: {phone}")

# Exit the bot
def close_command(args, contacts):
    print("Good bye!")
    return True

# For invalid commands
def invalid_command(args, contacts):
    print("Invalid command.")


def main():
    contacts = {}

    #show avaiable commands first
    print("Welcome to the assistant bot!")
    print("Available commands: hello, add, change, phone, all, exit / close")
    print()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # get the function from dictionary, default to invalid_command
        command_action = COMMANDS.get(command, invalid_command)

        should_exit = command_action(args, contacts)

        # only close_command returns True
        if should_exit:
            break

#add commands mapping to easier execution
COMMANDS = {
    "hello": hello_command,
    "add": add_contact,
    "change": change_command,
    "phone": phone_command,
    "all": all_command,
    "exit": close_command,
    "close": close_command
}

if __name__ == "__main__":
    main()
