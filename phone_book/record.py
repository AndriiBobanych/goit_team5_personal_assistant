from field import Field, Name, Phone, Email, Address, Birthday


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

