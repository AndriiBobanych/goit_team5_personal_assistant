from collections import UserDict
import pickle

from field import Field, Name, Phone, Email, Address, Birthday
from record import Record


class ContactBook(UserDict):
    __book_name = "contact_book.pickle"

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
                print("Contact-book was successfully saved")
        except Exception:
            print("Some problems arose during saving")

    def add_new_contact(self, name: Name, phone: Phone = None, email: Email = None,
                        address: Address = None, birthday: Birthday = None):
        new_contact = Record(name=name, phone=phone, email=email, address=address, birthday=birthday)
        self.data[name.value] = new_contact

    def find_by_name(self, key):
        matches = []
        for name in self.data.keys():
            if name.lower().find(key.lower()) != -1:
                matches.append(name)
        if matches == []:
            return "No mathes."
        result = ''
        for name in matches:
            result += str(self.data[name]) + '\n'
        return result
