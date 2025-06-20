from logic import * # importing logic

def main():
    ''' Command Line Interface bot '''
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input) 
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case 'phone':
                print(show_phone(args, contacts))
            case 'all':
                print(show_all(contacts))
            case _:
                print("Invalid command.")
if __name__ == "__main__":
    main()