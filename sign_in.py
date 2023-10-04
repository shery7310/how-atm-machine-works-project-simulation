import ast
import datetime
from random_account_maker import dictionary_handler, dictionary_writer, dictionary_updater


def account_detail(account, dictionary):
    """ Gives Account details taking account number and the dictionary as arguments"""
    branch, branch_code, name, account_opening_date, balance, currency, acc_status = \
        dictionary[account]["branch_name"], dictionary[account]["branch_code"], dictionary[account]["name"], \
            dictionary[account]["account_creation_date"], dictionary[account]["acc_details"]["balance_amount"], \
            dictionary[account]["acc_details"]['currency'], dictionary[account]["status"]
    last_transaction_amount = eval(tuple(dictionary[account]["acc_details"]["statement"].keys())[-1])
    last_transaction_string = ''
    if last_transaction_amount > 0 and dictionary[account]["acc_details"]["currency"] == "PKR":
        last_transaction_string = f'Rs.{last_transaction_amount} was/were credited at {tuple(dictionary[account]["acc_details"]["statement"].values())[-1]}'
    elif last_transaction_amount > 0 and dictionary[account]["acc_details"]["currency"] == "USD":
        last_transaction_string = f'${last_transaction_amount} was/were credited at {tuple(dictionary[account]["acc_details"]["statement"].values())[-1]}'
    elif last_transaction_amount < 0 and dictionary[account]["acc_details"]["currency"] == "PKR":
        last_transaction_string = f'Rs.{last_transaction_amount * -1} was/were debited at {tuple(dictionary[account]["acc_details"]["statement"].values())[-1]}'
    elif last_transaction_amount < 0 and dictionary[account]["acc_details"]["currency"] == "USD":
        last_transaction_string = f'${last_transaction_amount * -1} was/were debited at {tuple(dictionary[account]["acc_details"]["statement"].values())[-1]}'
    branch_Code = account[:4]
    remaining_account = account[4:]
    if dictionary[account]["acc_details"]["currency"] == "USD":
        balance_currency = "$"
    else:
        balance_currency = 'Rs.'
    return (
        branch, branch_Code + "-" + remaining_account, name, currency, account_opening_date, last_transaction_string,
        " " + balance_currency + balance, acc_status)


def deposit(account, dictionary, amount):
    """ Enter the amount you want to deposit and it will add that amount in statement and balance
    of already existing users"""
    if int(amount) < 0:
        raise ValueError("Remember You are depositing not withdrawing")
    current_balance = ast.literal_eval(dictionary[account]["acc_details"]["balance_amount"])
    current_balance += ast.literal_eval(amount)
    current_balance = str(current_balance)
    current_date_time = datetime.datetime.now()
    changed_format = current_date_time.strftime('%d-%h-%Y, %I:%M %p')

    str_amount = "+" + amount

    dictionary[account]["acc_details"]["balance_amount"] = current_balance
    dictionary[account]['acc_details']['statement'].update({str_amount: changed_format})
    print("Successfully deposited amount")
    dictionary_writer(dictionary)


def withdraw(account, dictionary, amount):
    """ Enter the amount you want to withdraw and it will subtract that amount + tax on it from statement and balance
        of already existing users"""
    current_balance = ast.literal_eval(dictionary[account]["acc_details"]["balance_amount"])
    amount = ast.literal_eval(amount)
    tax = (amount * (1 / 100))
    if current_balance < amount:
        return f"The balance in your account is less than the amount you want to withdraw, this is your balance: " \
               f"{current_balance}"
    else:
        if amount + tax < current_balance:
            current_balance -= amount + tax  # deducting tax from current balance
            current_balance = str(current_balance)
            str_amount = "-" + str(amount + tax)

        elif amount + tax > current_balance:
            current_balance -= amount  # deducting tax from the amount that user wants back
            amount -= tax  # deducting tax from amount
            amount = str(amount)
            current_balance = str(current_balance)
            str_amount = "-" + str(amount)

    current_date_time = datetime.datetime.now()
    changed_format = current_date_time.strftime('%d-%h-%Y, %I:%M %p')

    dictionary[account]["acc_details"]["balance_amount"] = current_balance
    dictionary[account]['acc_details']['statement'].update({str_amount: changed_format})
    print(f"You get: {amount}")
    dictionary_writer(dictionary)
    return f"This is your balance after withdrawing {current_balance}"


def update_pin(account, dictionary, pin):
    """ Update Pin of already existing users"""
    dictionary[account]['pin_code'] = pin
    dictionary_writer(dictionary)
    print("Successfully Updated Your Secret Code")


def check_statement(account, dictionary):
    """ Check statement of existing users"""
    user_id, account_string, statement_date = dictionary[account]['username'], account[:4] + "-" + account[4:],\
        datetime.datetime.now()

    from_date = tuple(dictionary[account]['acc_details']['statement'].values())[0].split(",")[0]  # 08-Sep-2023
    to_date = tuple(dictionary[account]['acc_details']['statement'].values())[-1].split(",")[0]
    balance = dictionary[account]['acc_details']['balance_amount']
    print(f"Statement Made on {statement_date.strftime('%d/%h/%Y at %I:%M %p')}", end="\n\n")  # 09/Sep/2023, at 06:21 PM
    print("******Screen Dump for Internal Use Only******")
    print(f"From: {from_date} \t\t To: {to_date}", end="\n\n")
    print("Posting Date", "Debit", "Credit", sep="\t\t")
    statement_dict = dictionary[account]['acc_details']['statement']
    for amount, posting_date in statement_dict.items():
        if '+' in amount:
            credit = amount[1:]
            debit = " "
        elif '-' in amount:
            debit = amount[1:]
            credit = " "

        print(posting_date.split(",")[0] + "         " + debit + "           " + credit, sep="")