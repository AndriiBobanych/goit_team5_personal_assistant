import functools


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

