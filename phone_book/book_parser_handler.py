from decorators import parser_error_handler, command_error_handler
from validators import phone_validity, email_validity, birthday_validity
from phone_book.contact_book import ContactBook
from phone_book.field import Name, Phone, Address, Email, Birthday

book_commands_dict = {
    "help",
    "back",
    "add",
    "change",
    "delete",
    '''
    "add contact",
    "add phone",
    "add email",
    "add address",
    "add birthday",
    "change phone",
    "change email",
    "change address",
    "delete contact",
    "delete phone",
    "delete email",
    "delete address",
    "delete birthday",
    '''
    "days to birthday",
    "phone",
    "find",
    "show all",
    "close",
    }


class PhonebookInputParser:

    @parser_error_handler
    def parse_user_input(self, user_input: str) -> tuple[str, list]:
        for command in book_commands_dict:
            normalized_input = " ".join(user_input.lower().strip().split(" "))
            if normalized_input.startswith(command):
                parser = getattr(self, "_" + command.replace(" ", "_"))
                return parser(user_input=normalized_input)
        raise ValueError

    def _help(self, user_input: str):
        return "help", []

    def _back(self, user_input: str):
        return "back", []

    def _add(self, user_input: str):
        args = user_input.lstrip("add ")
        field_name, username, value = args.strip().split(" ")
        if field_name not in ("contact", "phone", "email", "address", "birthday"):
            raise ValueError
        if field_name == "contact":
            if username == "":
                raise ValueError("Bad input")
            return "add_contact", [username]
        if username != "" and value != "":
            return f"add_{field_name}", [username, value] 
        else:
            raise ValueError

    def _change(self, user_input: str):
        args = user_input.lstrip("change ")
        field_name, username, value, new_value = args.strip().split(" ")
        if field_name not in ("phone", "email", "address"):
            raise ValueError
        if username != "" and value != "" and new_value != "":
            return f"change_{field_name}", [username, value, new_value] 
        else:
            raise ValueError

    def _delete(self, user_input: str):
        args = user_input.lstrip("delete ")
        field_name, username, value = args.strip().split(" ")
        if field_name not in ("contact", "phone", "email", "address", "birthday"):
            raise ValueError
        if field_name == "contact":
            if username == "":
                raise ValueError
            return "delete_contact", [username]
        if username != "" and value != "":
            return f"delete_{field_name}", [username, value] 
        else:
            raise ValueError

    def _days_to_birthday(self, user_input: str):
        return 'add', []

    def _phone(self, user_input: str):
        return 'add', []

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
    - add contact "name" "phone-number" "*birthday" -> to add new contact to your phonebook 
                                                       (*birthday also could be indicated, as option);
    - add phone "name" "phone-number" -> to add a phone for existing contact with this name;
    - add birthday "name" "birthday" -> to set up new (or change existing) birthday for contact with this name;
    - change phone "name" "old-phone" "new-phone" -> to set up new number for contact with this name;
    - delete contact "name" -> to delete the contact with this name from phonebook (if exist);
    - delete phone "name" "phone-number" -> to delete phone from the contact with this name;
    - delete birthday "name" -> to delete the birthday from the contact with this name;
    - days to birthday "name" -> to check how many days are left fot the contact's birthday (if indicated b/d);
    - phone "name" -> to see the phone numbers for the contact with this name (if exist);
    - show all -> to see all contacts in your phonebook (if you have added at least 1);
    - find "name" or "phone" -> to find contacts that are matching to entered key-letters or key-digits;
    - good bye / close / exit -> to finish work and close session;
    """

    @command_error_handler 
    def back_handler(self, *args):
        pass

    @command_error_handler 
    def add_contact_handler(self, username):
        if self._book.find_by_name(username) == "No mathes.":
            phone = input("Please enter phone: ")
            email = input("Please enter email: ")
            address = input("Please enter address: ")
            birthday = input("Please enter birthday: ")
            self._book.add_new_contact(name=Name(username), phone = Phone(phone), email=Email(email),
                 address=Address(address), birthday=Birthday(birthday))
            return "Contact was added."
        raise ValueError("You already add this contact.")

    @command_error_handler 
    def add_phone_handler(self, username, value):
        if self._book.find_by_name(username) == "No mathes.":
            self._book.add_record(name=Name(username), phone=Phone(value))
            return "Number was added."
        else:
            self._book[username].add_to_phone_field(Phone(value))
            return "Number was added."

    @command_error_handler 
    def add_email_handler(self, username, value):
        if self._book.find_by_name(username) == "No mathes.":
            self._book.add_record(name=Name(username), email=Email(value))
            return "Email was added."
        else:
            self._book[username].add_to_email_field(Email(value))
            return "Email was added."

    @command_error_handler 
    def add_address_handler(self, username, value):
        if self._book.find_by_name(username) == "No mathes.":
            self._book.add_record(name=Name(username), address=Address(value))
            return "Address was added."
        else:
            self._book[username].add_to_address_field(Address(value))
            return "Address was added."

    @command_error_handler 
    def add_birthday_handler(self, username, value):
        if self._book.find_by_name(username) == "No mathes.":
            self._book.add_record(name=Name(username), birthday=Birthday(value))
            return "Birthday was added."
        else:
            self._book[username].add_to_birthday_field(Birthday(value))
            return "Birthday was added."

    @command_error_handler 
    def change_phone_handler(self, username, value, new_value):
        if self._book.find_by_name(username) == "No mathes.":
            return "Contact does not exists!"
        else:
            return self._book.change_phone(Phone(value), Phone(new_value))        

    @command_error_handler 
    def change_email_handler(self, username, value, new_value):
        if self._book.find_by_name(username) == "No mathes.":
            return "Contact does not exists!"
        else:
            return self._book.change_email(Email(value), Email(new_value))    

    @command_error_handler 
    def change_address_handler(self, username, value, new_value):
        if self._book.find_by_name(username) == "No mathes.":
            return "Contact does not exists!"
        else:
            return self._book.change_address(Address(value), Address(new_value))    

    @command_error_handler 
    def delete_contact_handler(self, *args):
        pass

    @command_error_handler 
    def delete_phone_handler(self, *args):
        pass

    @command_error_handler 
    def delete_email_handler(self, *args):
        pass

    @command_error_handler 
    def delete_address_handler(self, *args):
        pass

    @command_error_handler 
    def delete_birthday_handler(self, *args):
        pass

    @command_error_handler 
    def days_to_birthday_handler(self, *args):
        pass

    @command_error_handler 
    def phone_handler(self, *args):
        pass

    @command_error_handler 
    def find_handler(self, *args):
        pass

    @command_error_handler 
    def show_all_handler(self, *args):
        pass

    @command_error_handler 
    def close(self, *args):
        pass
    
    def setup_book(self, book):
        self._book = book

    def run(self):

        with ContactBook() as book:
            self.setup_book(book)

            print('It is Your Contact Book. You can enter "help" to get a list of commands, "back" - return to main menu.')
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
