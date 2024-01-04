class PhoneNumber:
    def __init__(self, number, fio):
        if isinstance(number, int) and isinstance(fio, str):
            if len(str(number)) == 11:  # Check if the phone number has 11 digits
                self.number = number
                self.fio = fio
            else:
                raise ValueError("Phone number must have exactly 11 digits.")
        else:
            raise TypeError("Invalid data types for PhoneNumber attributes.")


class PhoneBook:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        if type(phone) == PhoneNumber:
            self.phones.append(phone)
        return self.phones

    def remove_phone(self, indx):
        if 0 <= indx <= len(self.phones):
            self.phones.pop(indx)
        return self.phones

    def get_phone_list(self):
        return self.phones


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "fio_1"))
p.add_phone(PhoneNumber(21345678901, "fio_2"))
p.remove_phone(0)
print(p.get_phone_list())
