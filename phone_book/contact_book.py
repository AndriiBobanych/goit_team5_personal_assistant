from collections import UserDict
import pickle

from field import Field, Name, Phone, Email, Address, Birthday
from record import Record


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
