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

    def add_to_phone_field(self, phone_number: Phone):
        self.phone.append(phone_number)

    def add_to_email_field(self, email: Email):
        self.email.append(email)

    def add_to_address_field(self, address: Address):
        self.address.append(address)

    def add_to_birthday_field(self, birthday: Birthday):
        self.birthday = birthday

    def change_phone(self, old_number: Phone, new_number: Phone):
        try:
            self.phone.remove(old_number)
            self.phone.append(new_number)
        except ValueError:
            return f"Contact does not contain such phone number: {old_number}"

    def change_email(self, old_email: Email, new_email: Email):
        try:
            self.email.remove(old_email)
            self.email.append(new_email)
        except ValueError:
            return f"Contact does not contain such email: {old_email}"

    def change_address(self, old_address: Address, new_address: Address):
        try:
            self.address.remove(old_address)
            self.address.append(new_address)
        except ValueError:
            return f"Contact does not contain such address: {old_address}"

    def delete_phone(self, phone: Phone):
        try:
            self.phone.remove(phone)
        except ValueError:
            print(f"Contact does not contain such phone number: {phone}")

    def delete_email(self, email: Email):
        try:
            self.email.remove(email)
        except ValueError:
            print(f"Contact does not contain such email: {email}")

    def delete_address(self, address: Address):
        try:
            self.address.remove(address)
        except ValueError:
            print(f"Contact does not contain such address: {address}")

    def delete_birthday(self):
        self.birthday.value = None

