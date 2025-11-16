from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            parsed = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(parsed)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old, new):
        if not self.remove_phone(old):
            raise ValueError("Old phone not found.")
        self.add_phone(new)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = ", ".join(str(p) for p in self.phones) if self.phones else "No phones"
        birthday = str(self.birthday) if self.birthday else "No birthday"
        return f"{self.name.value}: phones: {phones}; birthday: {birthday}"


# ============ Адресна книга ============

class AddressBook(dict):

    def add_record(self, record: Record):
        self[record.name.value] = record

    def find(self, name):
        return self.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        end_range = today + timedelta(days=7)

        congratulations = []

        for record in self.values():
            if not record.birthday:
                continue

            bday_date = record.birthday.value.date()
            bday_this_year = bday_date.replace(year=today.year)

            if today <= bday_this_year <= end_range:
                congratulations.append({
                    "name": record.name.value,
                    "birthday": bday_this_year.strftime("%d.%m.%Y")
                })

        return congratulations


# ============ Декоратор ============

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Not enough arguments."
    return wrapper


# ============ Парсер ============

def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


# ============ Обробка команд ============

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)

    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old, new = args
    record = book.find(name)
    if record is None:
        raise KeyError

    record.edit_phone(old, new)
    return "Phone updated."


@input_error
def show_phones(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    return ", ".join(str(p) for p in record.phones)


@input_error
def show_all(book):
    if not book:
        return "No contacts found."
    return "\n".join(str(record) for record in book.values())


@input_error
def add_birthday(args, book):
    name, date = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.add_birthday(date)
    return "Birthday added."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record is None or not record.birthday:
        return "Birthday not set."
    return str(record.birthday)


@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."

    return "\n".join(f"{u['name']}: {u['birthday']}" for u in upcoming)


# ============ Основний цикл ============

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phones(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
