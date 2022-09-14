from decorators import parser_error_handler, command_error_handler
from validators import phone_validity, email_validity, birthday_validity
from contact_book import ContactBook
from field import Name, Phone, Address, Email, Birthday

book_commands_dict = {
    "help",
    "add",
    "change",
    "delete",
    "nearby birthday",
    "find",
    "show all",
    "close",
    }


class PhonebookInputParser:

    @parser_error_handler
    def parse_user_input(self, user_input: str) -> tuple[str, list]:
        for command in book_commands_dict:
            normalized_input = " ".join(user_input.strip().split(" "))
            #normalized_input = " ".join(user_input.lower().strip().split(" "))
            if normalized_input.startswith(command):
                parser = getattr(self, "_" + command.replace(" ", "_"))
                return parser(user_input=normalized_input)
        raise ValueError

    def _help(self, user_input: str):
        return "help", []

    def _add(self, user_input: str):
        command = user_input.strip().split(" ")
        field_name = command[1]
        if field_name not in ("contact", "phone", "email", "address", "birthday"):
            raise ValueError
        if field_name == "contact":
            return "add_contact", []
        elif field_name == "address":
            if len(command) != 3:
                raise ValueError
            username = command[2]
            return f"add_address", [username]
        else:
            if len(command) != 4:
                raise ValueError 
            username, value = command[2:]
            return f"add_{field_name}", [username, value] 

    def _change(self, user_input: str):
        command = user_input.strip().split(" ")
        field_name = command[1]
        if field_name not in ("phone", "email", "address"):
            raise ValueError
        if field_name == "address":
            if len(command) != 3:
                raise ValueError
            username = command[2]
            return f"change_address", [username]
        else:
            if len(command) != 5:
                raise ValueError 
            username, value, new_value = command[2:]
            return f"change_{field_name}", [username, value, new_value] 

    def _delete(self, user_input: str):
        command = user_input.strip().split(" ")
        field_name = command[1]
        if field_name not in ("contact", "phone", "email", "address", "birthday"):
            raise ValueError
        if field_name in ("contact", "birthday"):
            if len(command) != 3:
                raise ValueError
            username = command[2]
            return f"delete_{field_name}", [username]
        else:
            if len(command) != 4:
                raise ValueError 
            username, value = command[2:]
            return f"delete_{field_name}", [username, value] 

    def _nearby_birthday(self, user_input: str):
        command = user_input.strip().split(" ")
        if len(command) != 3:
            raise ValueError
        days = int(command[2])
        return 'nearby_birthday', [days]

    def _find(self, user_input: str):
        input_list = user_input.lstrip("find ").strip().split(" ")
        pattern = input_list[0]
        if len(pattern) > 0:
            return "find", [pattern]
        else:
            raise ValueError

    def _show_all(self, user_input: str):
        if user_input.lower().strip() == "show all":
            return "show all", []
        else:
            raise ValueError

    def _close(self, user_input: str):    
        if user_input.lower().strip() in ("good bye", "close", "exit"):
            return "exit", []
        else:
            raise ValueError

    def _good_bye(self, user_input: str):
        return self._exit(user_input)

    def _close(self, user_input: str):
        return self._exit(user_input)


class CLIphonebook:
    def __init__(self):
        self._book = None
        self._parsers = PhonebookInputParser()

    @command_error_handler 
    def help_handler(self, *args):
        return """You can use the following commands for your phonebook:
    //first command - than arguments//
    - add contact -> to add new contact to your phonebook 
    - add phone "name" "phone-number" -> to add a phone for existing contact or to add new contact with phone;
    - add email "name" "email" -> to add a email for existing contact or to add new contact with email;
    - add address "name" -> to add a address for existing contact or to add new contact with address;
    - add birthday "name" "birthday" -> to set up new (or change existing) birthday for contact with this name;

    - change phone "name" "old-phone" "new-phone" -> to set up new number for contact with this name;
    - change email "name" "old-email" "new-email" -> to set up new email for contact with this name;
    - change address "name" "old-address" "new-address" -> to set up new address for contact with this name;

    - delete contact "name" -> to delete the contact with this name from phonebook (if exist);
    - delete phone "name" "phone-number" -> to delete phone from the contact with this name;
    - delete email "name" "email" -> to delete email from the contact with this name;
    - delete address "name" "address" -> to delete address from the contact with this name;
    - delete birthday "name" -> to delete the birthday from the contact with this name;

    - nearby birthday "days" -> to show who celebrating birthdays in the next days;
    - show all -> to see all contacts in your phonebook (if you have added at least 1);
    - find "name" -> to find contacts that are matching to entered key-letters;
    - close -> to finish work and return to main menu;
    """

    @command_error_handler 
    def add_contact_handler(self):
        username = input("Please enter name: ")
        if self._book.find_by_name(username) == "No mathes.":
            phone = input("Please enter phone: ")
            if phone != '' and phone_validity(phone) == False: 
                return "\nIncorrect input. Try again.\n"
            email = input("Please enter email: ")
            if email != '' and email_validity(email) == False:
                return "\nIncorrect input. Try again.\n"
            address = input("Please enter address: ")
            birthday = input("Please enter birthday: ")
            if birthday != '' and birthday_validity(birthday) == False:
                return "\nIncorrect input. Try again. Birthday format: dd-mm-yyyy\n"
            self._book.add_new_contact(name=Name(username), phone=Phone(phone), email=Email(email),
                 address=Address(address), birthday=Birthday(birthday))
            return "Contact was added."
        raise ValueError("You already add this contact.")

    @command_error_handler 
    def add_phone_handler(self, username, value):
        if phone_validity(value) == False: 
                return "\nIncorrect input. Try again.\n"
        if self._book.find_by_name(username) == "No mathes.":
            self._book.add_new_contact(name=Name(username), phone=Phone(value))
        else:
            self._book[username].add_to_phone_field(Phone(value))
        return "Number was added."

    @command_error_handler 
    def add_email_handler(self, username, value):
        if email_validity(value) == False:
                return "\nIncorrect input. Try again.\n"
        if self._book.find_by_name(username) == "No mathes.":
            self._book.add_new_contact(name=Name(username), email=Email(value))
        else:
            self._book[username].add_to_email_field(Email(value))
        return "Email was added."

    @command_error_handler 
    def add_address_handler(self, username):
        value = input("Please enter address: ")
        if self._book.find_by_name(username) == "No mathes.":
            self._book.add_new_contact(name=Name(username), address=Address(value))
        else:
            self._book[username].add_to_address_field(Address(value))
        return "Address was added."

    @command_error_handler 
    def add_birthday_handler(self, username, value):
        if birthday_validity(value) == False:
                return "\nIncorrect input. Try again. Birthday format: dd-mm-yyyy\n"
        if self._book.find_by_name(username) == "No mathes.":
            self._book.add_new_contact(name=Name(username), birthday=Birthday(value))
        else:
            self._book[username].add_to_birthday_field(Birthday(value))
        return "Birthday was added."

    @command_error_handler 
    def change_phone_handler(self, username, value, new_value):
        if phone_validity(new_value) == False: 
                return "\nIncorrect input. Try again.\n"
        if self._book.find_by_name(username) == "No mathes.":
            return "Contact does not exists!"
        else:
            return self._book[username].change_phone(value, new_value)        

    @command_error_handler 
    def change_email_handler(self, username, value, new_value):
        if email_validity(new_value) == False: 
                return "\nIncorrect input. Try again.\n"
        if self._book.find_by_name(username) == "No mathes.":
            return "Contact does not exists!"
        else:
            return self._book[username].change_email(value, new_value)    

    @command_error_handler 
    def change_address_handler(self, username):
        if self._book.find_by_name(username) == "No mathes.":
            return "Contact does not exists!"
        else:
            value = input("Please enter old address: ")
            new_value = input("Please enter new address: ")
            return self._book[username].change_address(value, new_value)    

    @command_error_handler 
    def delete_contact_handler(self, username):
        if self._book.find_by_name(username) != "No mathes.":
            self._book.pop(username)
            return f"Contact '{username}' was deleted successfully from your phonebook"
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def delete_phone_handler(self, username, value):
        if self._book.find_by_name(username) != "No mathes.":
            return self._book[username].delete_phone(value)
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def delete_email_handler(self, username, value):
        if self._book.find_by_name(username) != "No mathes.":
            return self._book[username].delete_email(value)
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def delete_address_handler(self, username, value):
        if self._book.find_by_name(username) != "No mathes.":
            return self._book[username].delete_address(value)
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def delete_birthday_handler(self, username):
        if self._book.find_by_name(username) != "No mathes.":
            return self._book[username].delete_birthday()
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def nearby_birthday_handler(self, days):
        return self._book.nearby_birthday(days)

    @command_error_handler 
    def find_handler(self, pattern):
        return self._book.find_by_name(pattern)

    @command_error_handler 
    def show_all_handler(self, *args):
        return next(self._book_iterator)

    @command_error_handler 
    def close(self, *args):
        pass
    
    def setup_book(self, book):
        self._book = book

    def run(self):

        with ContactBook() as book:
            self.setup_book(book)
            self._book_iterator = iter(self._book)        

            print('It is Your Contact Book. You can enter "help" to get a list of commands, "close" - return to main menu.')
            while True:
                user_input = input("Please enter command: ")
                result = self._parsers.parse_user_input(user_input=user_input)
                if len(result) != 2:
                    print(result)
                    continue
                command, arguments = result
                command_function = getattr(self, command.replace(" ", "_") + "_handler")
                try:
                    command_response = command_function(*arguments)
                    print(command_response)
                except SystemExit as e:
                    print(str(e))
                    break

if __name__ == "__main__":
    cli = CLIphonebook()
    cli.run()