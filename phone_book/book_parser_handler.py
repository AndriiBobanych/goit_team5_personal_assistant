from decorators import parser_error_handler, command_error_handler
from validators import phone_validity, email_validity, birthday_validity

book_commands_dict = {
    "help",
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


class CLIphonebook:
    pass
