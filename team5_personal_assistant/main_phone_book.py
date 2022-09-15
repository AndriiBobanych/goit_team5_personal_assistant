# from contact_book import ContactBook
# from field import Name, Phone, Address, Email, Birthday
from collections import UserDict
import pickle
import functools
from datetime import datetime
import re


# -------------------------- class Field --------------------------


class Field:
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass


class Address(Field):
    pass


class Birthday(Field):
    pass


# -------------------------- class Record --------------------------


class Record:

    def __init__(self, name: Name, phone: Phone = None, email: Email = None,
                 address: Address = None, birthday: Birthday = None):
        self.name = name
        self.phone = [phone] if phone is not None else []
        self.email = [email] if email is not None else []
        self.address = [address] if address is not None else []
        self.birthday = birthday

    def __repr__(self):
        return f"name: {self.name.value}; " \
               f"phones: {' '.join(phone.value for phone in self.phone)}; " \
               f"emails: {' '.join(email.value for email in self.email)}; " \
               f"addresses: {' '.join(address.value for address in self.address)}; " \
               f"birthday: {self.birthday.value if self.birthday is not None else ''}"

    def add_to_phone_field(self, phone_number: Phone):
        self.phone.append(phone_number)

    def add_to_email_field(self, email: Email):
        self.email.append(email)

    def add_to_address_field(self, address: Address):
        self.address.append(address)

    def add_to_birthday_field(self, birthday: Birthday):
        self.birthday = birthday

    def change_phone(self, old_number, new_number):
        for p in self.phone:
            if p.value == old_number:
                p.value = new_number
                return 'Done!'
        return f"Contact does not contain such phone number: {old_number}"

    def change_email(self, old_email, new_email):
        for e in self.email:
            if e.value == old_email:
                e.value = new_email
                return 'Done!'
        return f"Contact does not contain such email: {old_email}"

    def change_address(self, old_address, new_address):
        for a in self.address:
            if a.value == old_address:
                a.value = new_address
                return 'Done!'
        return f"Contact does not contain such address: {old_address}"

    def delete_phone(self, phone):
        for p in self.phone:
            if p.value == phone:
                self.phone.remove(p)
                return 'Done!'
        return f"Contact does not contain such phone number: {phone}"

    def delete_email(self, email):
        for e in self.email:
            if e.value == email:
                self.email.remove(e)
                return 'Done!'
        return f"Contact does not contain such email: {email}"

    def delete_address(self, address: Address):
        for a in self.address:
            if a.value == address:
                self.address.remove(a)
                return 'Done!'
        return f"Contact does not contain such address: {address}"

    def delete_birthday(self):
        if self.birthday == None:
            return "Contact doesn't have birthday."
        self.birthday.value = None
        return "Done!"


# -------------------------- class ContactBook --------------------------


class ContactBook(UserDict):
    __book_name = "contact_book.pickle"
    __items_per_page = 10

    def items_per_page(self, value):
        self.__items_per_page = value

    items_per_page = property(fget=None, fset=items_per_page)

    def __enter__(self):
        self.__update()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__save()

    def __update(self):
        try:
            with open(self.__book_name, "rb+") as file:
                book = pickle.load(file)
                self.data.update(book)
        except Exception:
            return "Contact-book is not updated"

    def __save(self):
        try:
            with open(self.__book_name, "wb+") as file:
                pickle.dump(self.data, file, protocol=pickle.HIGHEST_PROTOCOL)
                return "Contact-book was successfully saved"
        except Exception:
            return "Some problems arose during saving"

    def add_new_contact(self, name: Name, phone: Phone = None, email: Email = None,
                        address: Address = None, birthday: Birthday = None):
        new_contact = Record(name=name, phone=phone, email=email, address=address, birthday=birthday)
        self.data[name.value] = new_contact

    def find_by_name(self, key):
        matches = []
        for name in self.data.keys():
            if name.lower().strip().find(key.lower().strip()) != -1:
                matches.append(name)
        if matches == []:
            return "No matches."
        result = ''
        for name in matches:
            result += str(self.data[name]) + '\n'
        return result

    def __iter__(self):
        self.page = 0
        return self

    def __next__(self):
        records = list(self.data.items())
        start_index = self.page * self.__items_per_page
        end_index = (self.page + 1) * self.__items_per_page
        page = self.page + 1
        if len(records) == 0:
            return 'Your phone book is empty.'
        if len(records) > end_index:
            to_return = records[start_index:end_index]
            self.page += 1
        else:
            if len(records) > start_index:
                to_return = records[start_index : len(records)]
                self.page = 0
            else:
                to_return = records[0:self.__items_per_page]
                self.page = 1
        result = f'   ---   Page {page}   ---   \n'
        for record in to_return:
            result += str(record[1]) + '\n'
        return result

    def nearby_birthday(self, n_days):
        now = datetime.now().timetuple().tm_yday
        future = now + int(n_days)
        new_year_future = 0
        if future > 365:
            new_year_future = future - 365
            future = 365
        fut_list = []
        for k, v in self.data.items():
                if v.birthday != None:
                    s = datetime.strptime(v.birthday.value,'%d-%m-%Y').timetuple().tm_yday
                    if future >= s >= now or 1 <= s <= new_year_future:
                        fut_list.append(f"{k}: {v.birthday.value}")
        if fut_list == []:
            return f'No contacts are celebrating their birthday in the next {n_days} days'
        else:
            result = f"Following users are celebrating birthdays in the next {n_days} days:\n"
            for name in fut_list:
                result += name + '\n'
        return result


# -------------------------- error handler decorators --------------------------


def parser_error_handler(func):
    @functools.wraps(func)
    def wrapper(self, user_input: str):
        try:
            return func(self, user_input)
        except ValueError as e:
            print("\nIncorrect input.\nPlease check details and enter correct command.")
            return str(e)
        except KeyError as e:
            print("\nIncorrect input.\nPlease check details and enter correct command.")
            return str(e)
        except TypeError as e:
            print("\nIncorrect input.\nPlease check details and enter correct command.")
            return str(e)
        except IndexError as e:
            print("\nIncorrect input.\nPlease check details and enter correct command.")
            return str(e)
    return wrapper


def command_error_handler(func):
    @functools.wraps(func)
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except Exception as e:
            return str(e)
    return wrapper


# -------------------------- phone email b/d validators --------------------------


def phone_validity(number: str):
    phone_number = (
        number.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if phone_number.isdigit() and phone_number.startswith("380") and len(phone_number) == 12:
        return True
    else:
        return False


def email_validity(email: str):
    input_email = email.strip()
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

    if re.match(pattern, input_email) is not None:
        return True
    else:
        return False


def birthday_validity(birthday: str):
    try:
        if datetime.strptime(str(birthday), "%d-%m-%Y").date():
            return True
    except ValueError:
        return False


# -------------------------- PhonebookInputParser --------------------------


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
        # if user_input not in book_commands_dict:
        #     list_comm = []
        #     for k in book_commands_dict:
        #         for item in k.split():
        #             if user_input in item:
        #                 list_comm.append(k)
        #                 break
        #     if list_comm:
        #         print('You mean these commands: ')
        #         print(*list_comm,sep=', ')
        #     else:
        #         print("Incorrect input.\nPlease check and enter correct command (or 'help' or 'close').")
        # else:
        for command in book_commands_dict:
            normalized_input = " ".join(user_input.strip().split(" "))
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
        if user_input.lower().strip() == "close":
            return "close", []
        else:
            raise ValueError

    # def _close(self, user_input: str):
    #     if user_input.lower().strip() in ("good bye", "close", "exit"):
    #         return "exit", []
    #     else:
    #         raise ValueError
    #
    # def _good_bye(self, user_input: str):
    #     return self._exit(user_input)
    #
    # def _close(self, user_input: str):
    #     return self._exit(user_input)


# -------------------------- class CLIPhoneBook --------------------------


class CLIPhoneBook:
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
        if self._book.find_by_name(username) == "No matches.":
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
        if self._book.find_by_name(username) == "No matches.":
            self._book.add_new_contact(name=Name(username), phone=Phone(value))
        else:
            self._book[username].add_to_phone_field(Phone(value))
        return "Number was added."

    @command_error_handler 
    def add_email_handler(self, username, value):
        if email_validity(value) == False:
                return "\nIncorrect input. Try again.\n"
        if self._book.find_by_name(username) == "No matches.":
            self._book.add_new_contact(name=Name(username), email=Email(value))
        else:
            self._book[username].add_to_email_field(Email(value))
        return "Email was added."

    @command_error_handler 
    def add_address_handler(self, username):
        value = input("Please enter address: ")
        if self._book.find_by_name(username) == "No matches.":
            self._book.add_new_contact(name=Name(username), address=Address(value))
        else:
            self._book[username].add_to_address_field(Address(value))
        return "Address was added."

    @command_error_handler 
    def add_birthday_handler(self, username, value):
        if birthday_validity(value) == False:
                return "\nIncorrect input. Try again. Birthday format: dd-mm-yyyy\n"
        if self._book.find_by_name(username) == "No matches.":
            self._book.add_new_contact(name=Name(username), birthday=Birthday(value))
        else:
            self._book[username].add_to_birthday_field(Birthday(value))
        return "Birthday was added."

    @command_error_handler 
    def change_phone_handler(self, username, value, new_value):
        if phone_validity(new_value) == False: 
                return "\nIncorrect input. Try again.\n"
        if self._book.find_by_name(username) == "No matches.":
            return "Contact does not exists!"
        else:
            return self._book[username].change_phone(value, new_value)        

    @command_error_handler 
    def change_email_handler(self, username, value, new_value):
        if email_validity(new_value) == False: 
                return "\nIncorrect input. Try again.\n"
        if self._book.find_by_name(username) == "No matches.":
            return "Contact does not exists!"
        else:
            return self._book[username].change_email(value, new_value)    

    @command_error_handler 
    def change_address_handler(self, username):
        if self._book.find_by_name(username) == "No matches.":
            return "Contact does not exists!"
        else:
            value = input("Please enter old address: ")
            new_value = input("Please enter new address: ")
            return self._book[username].change_address(value, new_value)    

    @command_error_handler 
    def delete_contact_handler(self, username):
        if self._book.find_by_name(username) != "No matches.":
            self._book.pop(username)
            return f"Contact '{username}' was deleted successfully from your phonebook"
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def delete_phone_handler(self, username, value):
        if self._book.find_by_name(username) != "No matches.":
            return self._book[username].delete_phone(value)
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def delete_email_handler(self, username, value):
        if self._book.find_by_name(username) != "No matches.":
            return self._book[username].delete_email(value)
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def delete_address_handler(self, username, value):
        if self._book.find_by_name(username) != "No matches.":
            return self._book[username].delete_address(value)
        else:
            raise ValueError(f"Contact with name '{username}' does not exist in phonebook.")

    @command_error_handler 
    def delete_birthday_handler(self, username):
        if self._book.find_by_name(username) != "No matches.":
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
    def close_handler(self, *args):
        raise SystemExit("\nThank you for using ContactBook Bot.\nSee you later!\n")

    def setup_book(self, book):
        self._book = book

    def run_phone_assistant(self):

        with ContactBook() as book:
            self.setup_book(book)
            self._book_iterator = iter(self._book)

            print('It is Your Contact Book.\n'
                  'You can enter "help" to get a list of commands, "close" - return to main menu.')

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
                    return str(e)
                    # print(str(e))
                    # break

        # with ContactBook() as book:
        #     self.setup_book(book)
        #     self._book_iterator = iter(self._book)
        #
        #     print('It is Your Contact Book.\n'
        #           'You can enter "help" to get a list of commands, "close" - return to main menu.')
        #     while True:
        #         user_input = input("Please enter command: ")
        #
        #         if user_input == "close":
        #             raise SystemExit("\nThank you for using NoteBook.\nSee you later!\n")
        #
        #         elif user_input.split() != 2:
        #             list_comm = []
        #             for k in book_commands_dict:
        #                 for item in k.split():
        #                     if user_input in item:
        #                         list_comm.append(k)
        #                         break
        #
        #             if list_comm:
        #                 print('You mean these commands: ')
        #                 print(*list_comm,sep=', ')
        #             else:
        #                 print("Incorrect input.\nPlease check and enter correct command (or 'help' or 'close').")
        #
        #         else:
        #             result = self._parsers.parse_user_input(user_input=user_input)
        #             command, arguments = result
        #             command_function = getattr(self, command.replace(" ", "_") + "_handler")
        #             command_response = command_function(*arguments)
        #             print(command_response)


# def run_phone_assistant():
#     ph_bot = CLIPhoneBook()
#     ph_bot.run_phone_assistant()


if __name__ == "__main__":
    cli = CLIPhoneBook()
    cli.run_phone_assistant()

