# goit-pycore-hw-07 - Assistant Bot

A console-based personal assistant bot built in Python.  

---

## Features

- Add new contactss
- Update phone numbers
- Validate phone numbers (exactly 10 digits)
- Add and display birthdays in **DD.MM.YYYY** format
- Validate birthday date format
- Show all contacts
- Display upcoming birthdays within the next week
- Graceful exit via `close` or `exit`

---

## Commands

| Command | Description |
|--------|-------------|
| `add [name] [phone]` | Add a new contact or add a phone to an existing contact |
| `change [name] [old phone] [new phone]` | Change a contact’s phone number |
| `phone [name]` | Show phone numbers of the contact |
| `all` | Show all saved contacts |
| `add-birthday [name] [DD.MM.YYYY]` | Add birthday to a contact |
| `show-birthday [name]` | Show the contact’s birthday |
| `birthdays` | Show upcoming birthdays for next 7 days |
| `hello` | Bot greeting |
| `close` / `exit` | Quit the program |

---

## Data Validation

- **Phone** must be exactly **10 digits**
- **Birthday** must be formatted as **DD.MM.YYYY**

---

## Run

```bash
python assistant_bot.py
```

Then type commands directly into the console.

---

## Project Structure

```
assistant_bot.py
README.md
```

---

## Example 

```
Enter a command: add John 0931234567
Contact added.

Enter a command: add-birthday John 12.04.1990
Birthday added.

Enter a command: show-birthday John
12.04.1990

Enter a command: birthdays
No birthdays in the next 7 days.
```

---

## Requirements

- All required commands implemented
- Validation added
- Informative error messages via decorator
- Uses `AddressBook`, `Record`, `Birthday`, `Phone`, `Name`
- Proper program exit handling


