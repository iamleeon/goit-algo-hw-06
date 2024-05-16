from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.phone_validation(value):
            raise ValueError("Invalid phone format")
        super().__init__(value)

    def phone_validation(self, phone):
        if len(phone) == 10 and int(phone) != True:
            return phone
        else:
            return None


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone_to_remove):
        self.phones = [phone for phone in self.phones if phone.value != phone_to_remove]

    def edit_phone(self, old_phone, new_phone):
        new_phone = Phone(new_phone)
        self.phones = [new_phone if phone.value == old_phone else phone for phone in self.phones]

    def find_phone(self, phone):
        for p in self.phones:
            if phone == str(p):
                return p

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        del self.data[name]
