from collections import UserDict
import re


class Field:
    pass


class Name(Field):
    def __init__(self, param):
        self.param = param


class Phone(Field):
    def __init__(self, param):
        self._param = None
        self.param = param
        print(f'!!!!МОТРИ СЮДА {param}')

    def __repr__(self):
        return f'{self.param}'

    # !! Проверку на корректность веденного номера телефона в setter для value класса Phone.
    # def phone_setter(self, param, result):
    #   for
    @property
    def param(self):  # Смотри сюда, метод должен называться по именю поля!
        return self._param

    # a setter function
    @param.setter
    def param(self, data):
        if len(data) == 13 or data.startswith('+380'):
            self._param = data
        else:
            raise ValueError("Phone is incorrect. Please enter phone in +380.. format. It's length should be 13 chars")
        print("setter method called")


class Birthday(Field):
    def __init__(self, param):
        self._param = None
        self.param = param

    @property
    def param(self):
        print("!!!2test{b_day}")
        return self._param

    @param.setter
    def param(self, data):
        match = re.search(r'\d{2}.\d{2}.\d{4}', data)
        if match:
            self._param = data
            print('Пыщ-Пыщ')  # ОН ТАК И НЕ ВЫЗВАЛСЯ
        else:
            raise ValueError("Birthday format issue. Please enter b-day in DD.MM.YY format")
        print("setter method called")


class Record:
    def __init__(self, name, phone=None, b_day=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def __repr__(self):
        return f'{self.phones}'

    def addPhone(self, phone: Phone):
        self.phones.append(phone)

    def erasePhone(self, phone: Phone):
        for p in self.phones:
            if p.param == phone.param:
                self.phones.remove(p)

    def changePhone(self, phone: Phone, new_phone: Phone):
        for p in self.phones:
            if p.param == phone.param:
                self.erasePhone(p)
                self.addPhone(new_phone)

    # !!!!!Add functional working with Birthdays
    def days_to_birthday(self, b_day):
        # get this_b_day
        # next_b_day = this_b_day + 1 year
        # convert this_b_day to days
        # convert next_b_day to days
        # return next_b_day to days - this_b_day to days
        pass


class AddressBook(UserDict):
    # !!! Add optiona value: Birthday
    def add_record(self, rec, b_day=None):
        self.data[rec.name.param] = rec

    def iterator(self):
        pass
    # !!!! Vallidation of phone and birthday
    # !!! AddressBook p


# Phonebook is now a tuple
phone_book = AddressBook()


def add(*args):
    name = Name(args[0])
    try:
        phone = Phone(args[1])
    except ValueError as e:
        return e
    try:
        b_day = Birthday(args[2])
    except IndexError:
        b_day = None
    except ValueError as e:
        return e
    rec = Record(name, phone, b_day)
    phone_book.add_record(rec)
    print(phone_book)
    return f'Contact {name.param} add successful'


def erase_phone(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    print(f'!!!!!{args[1]}     {name} ')
    rec = phone_book[name.param]
    if rec:
        rec.erasePhone(phone)
    print(phone_book)
    return f'Contact {phone.param} erase successful'


def adds_phone(*args):
    key = args[0]
    phone = Phone(args[1])
    value = phone_book.get(key)
    if value:
        value.addPhone(phone)
        print(phone_book)
    return phone_book


def change_phone(*args):
    key = args[0]
    phone = Phone(args[1])
    value = phone_book.get(key)
    new_phone = Phone(args[2])
    if new_phone:
        value.changePhone(phone, new_phone)
        print(f'Contact {value} changed successful')
    print(phone_book)
    return phone_book


def exit(*args):
    return "Good bye!"


COMMANDS = {
    add: ["add"],
    adds_phone: ['append phone'],
    erase_phone: ["erase"],  # in command enter command, user, phone number to erase
    change_phone: ["change phone"],
    # days to birthday call
    exit: ["good bye", "close", "exit"]
}


def parse_command(user_input: str):
    for komand, v in COMMANDS.items():
        count = 0
        b_day = None
        for i in v:
            if count == 2:
                b_day = i
            if user_input.lower().startswith(i.lower()):
                data = user_input[len(i):].strip().split(" ")
            count += 1
        return komand, data, b_day


def main():
    while True:
        user_input = input('Please enter your command in format command -> User -> phone number -> birthday date')
        result, data, b_day = parse_command(user_input)
        print(result(*data))
        if result is exit:
            break


if __name__ == '__main__':
    main()