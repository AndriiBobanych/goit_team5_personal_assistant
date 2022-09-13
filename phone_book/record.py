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
        '''
        try:
            self.phone.remove(phone)
        except ValueError:
            print(f"Contact does not contain such phone number: {phone}")
        '''

    def delete_email(self, email):
        for e in self.email:
            if e.value == email:
                self.email.remove(e) 
                return 'Done!'
        return f"Contact does not contain such email: {email}"
        '''
        try:
            self.email.remove(email)
        except ValueError:
            print(f"Contact does not contain such email: {email}")
        '''

    def delete_address(self, address: Address):
        for a in self.address:
            if a.value == address:
                self.address.remove(a) 
                return 'Done!'
        return f"Contact does not contain such address: {address}"
        '''
        try:
            self.address.remove(address)
        except ValueError:
            print(f"Contact does not contain such address: {address}")
        '''

    def delete_birthday(self):
        if self.birthday == None:
            return "Contact doesn't have birthday."
        self.birthday.value = None
        return "Done!"

