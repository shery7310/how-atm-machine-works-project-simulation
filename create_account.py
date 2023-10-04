import random
from datetime import datetime
from random_account_maker import dictionary_handler, dictionary_writer, dictionary_updater, account_number_creator

branch_codes = {
    '0435': 'Chakira Branch, Fsd',
    '0419': 'Circular Road Branch, Fsd',
    '0406': 'Dijkot Road Branch, Fsd',
    '0431': 'Eden Square Branch, Fsd',
    '0220': 'Zarrar Shaheed Road Branch, Lhr',
    '1146': 'Askari X Branch, Lhr',
    '0255': 'Model Town K Block Branch, Lhr',
    '0276': 'Chungi Amar Sadhu Branch, Lhr',
    '0262': 'New Fruit Market Branch, Lhr',
    '0416': 'Canal Road Branch, Fsd'
}

random_number = random.randint(100, 9999999)


# These are handled by exceptions

def name_getter():
    """Returns Name"""

    name = input("Enter First Name: ").capitalize()
    lastname = input("Enter Last Name: ").capitalize()
    complete_name = name + " " + lastname

    try:
        if not name.isalpha():
            raise ValueError("Enter Alphabets Only, as first name")
        if not lastname.isalpha():
            raise ValueError("Enter Alphabets Only, as last name")

        return complete_name

    except ValueError as e:
        print(e)
        return

    except Exception as e:
        print("Unknown error occurred")
        return


def pin_code_getter():
    """Returns pin_code as a string"""

    try:
        pin_code = input("Enter 4 Digit Pin Number: ")
        if not pin_code.isnumeric():
            raise ValueError("Enter Digits Only")
        if len(pin_code) != 4:
            raise ValueError("Enter 4 Digits Only")

        return pin_code

    except ValueError as e:
        print(e)
        return

    except Exception as e:
        print("Unknown error occurred")
        return


def currency_getter():
    """Returns currency as string i.e USD or PKR"""

    try:
        currency = input("Enter D for Dollar or P for PKR Currency: ").lower()
        if currency not in ["d", "p"]:
            raise ValueError("Enter D or P only")

        if currency == "d":
            return "USD"
        elif currency == "p":
            return "PKR"

    except ValueError as e:
        print(e)
        return

    except Exception as e:
        print("Unknown error occurred")
        return


def deposit_amount_getter():
    """ Returns amount the user wants to deposit, only multiples of 500 and minimum amount is 2000 as a string"""

    try:
        amount = float(input("Enter Multiples of 500 to deposit, minimum amount 2000: "))
        if amount < 2000:
            raise ValueError("Amount should be greater than 2000 and multiple of 500 for account opening")
        elif amount > 2000:
            if amount % 500 != 0:
                raise ValueError("Amount should be greater than 2000 and multiple of 500 for account opening")
        return str(amount)

    except TypeError:
        print("Enter a number only")
        return

    except ValueError as e:
        print(e)
        return

    except Exception as e:
        print("Unknown error occurred")
        return


def cell_number_getter():
    """ Returns 11 digit cell number as a string"""

    try:
        cell_number = input("Enter 11 Digit Phone Number: ")
        if not cell_number.isnumeric():
            raise ValueError("Enter numbers not characters or alphabets")
        if len(cell_number) != 11:
            raise ValueError("Enter 11 Numbers only")

        return cell_number

    except ValueError as e:
        print(e)
        return

    except Exception as e:
        print("Unknown error occurred")
        return


def branch_getter():
    """ Returns Branch Code and Name as tuple"""

    try:
        print("Enter branch codes only from these codes:")
        for code in branch_codes:
            print(code)

        code = input("Enter your branch code: ")
        if code not in branch_codes:
            raise ValueError("Enter the correct code")

        name = branch_codes[code]
        return code, name

    except ValueError as e:
        print(e)
        return

    except Exception as e:
        print("Unknown error occurred")
        return


def sign_up():
    """ Returns something like
    # ('Firstname Lastname', '1234', 'PKR', '2500.0', '03228669111', ('0416', 'Canal Road Branch, # Fsd'))
    """
    name, pin_code, currency, amount, cell_number, branch = None, None, None, None, None, None
    try:
        while name is None:
            name = name_getter()
        while pin_code is None:
            pin_code = pin_code_getter()
        while currency is None:
            currency = currency_getter()
        while amount is None:
            amount = deposit_amount_getter()
        while cell_number is None:
            cell_number = cell_number_getter()
        while branch is None:
            branch = branch_getter()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print("Something went wrong")
    else:
        return name, pin_code, currency, amount, cell_number, branch

# these are not handled by exceptions


def account_creator():
    """ Runs a loop that fetches details from signup function, if there is an exception it will ask the user to enter that specific user"""
    while True:
        details = sign_up()
        if details is not None:
            if len(details) == 6:
                break
    return details


def account_creation(creator):
    """ Will return a dictionary to create a new user"""
    details = creator
    name = details[0]  # fullname
    branch_code = details[5][0]  # 0416
    branch_name = details[5][1]  # Canal Road Branch, Fsd
    pin_code = details[1]  # 4524
    status = "Active"
    account_creation_date = datetime.now()
    statement_first_value_date = account_creation_date
    account_creation_date = account_creation_date.strftime('%A, %d-%h-%Y, %I:%M %p')  # Thursday, 30-Mar-2000, 09:34 AM
    # %A - Weekday name, %d - Day of month, %A - Weekday name, %d - Day of month, %h - Abbreviated month name,
    # %Y - Year, %I - 12 hour clock hour, %M - Minutes, %p - AM/PM
    statement_first_value_date = statement_first_value_date.strftime('%d-%h-%Y, %I:%M %p')  # 30-Mar-2000, 09:34 AM
    cell_number = details[4]
    currency = details[2]
    balance_amount = details[3]
    # statement = {f'+{balance_amount}': statement_first_value_date}
    account = account_number_creator(branch_code)
    if account in dictionary_handler().keys():
        account = account_number_creator(branch_code)
        account = account[0]
        print("I ran")
    account = account[0]
    username = details[0].split(" ")[0]  # firstname
    username += str(random_number)

    new_user = {account: {"name": name, "username": username, 'branch_code': branch_code,
                          "branch_name": branch_name, "pin_code": pin_code,
                          "status": status, "account_creation_date": account_creation_date, "cell_number": cell_number,
                          "acc_details": {'statement': {f'+{balance_amount}': statement_first_value_date},
                                          "balance_amount": f'{balance_amount}', "currency": currency,
                                          }
                          }
                }
    return new_user





