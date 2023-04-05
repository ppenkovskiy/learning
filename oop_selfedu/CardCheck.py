from string import ascii_lowercase

class CardCheck:
    @staticmethod
    def check_card_number(number):
        number = list(str(number))
        for i in range(len(number)):
            if number[i].isdigit():
                number[i] = 'X'
        return ''.join(number) == 'XXXX-XXXX-XXXX-XXXX'

    @staticmethod
    def check_name(name):
        digits = '1234567890'
        CHARS_FOR_NAME = ascii_lowercase.upper() + digits
        if name.count(' ') != 1:
            return False
        name = name.replace(' ', '')
        for i in name:
            if i not in CHARS_FOR_NAME:
                return False
        return True


number = '1111-1111-1111-1111'
print(CardCheck.check_card_number(number))
name_1 = 'Pavel Penkovskiy'
name_2 = 'PAVEL PENKOVSKIY'
print(CardCheck.check_name(name_1))
print(CardCheck.check_name(name_2))