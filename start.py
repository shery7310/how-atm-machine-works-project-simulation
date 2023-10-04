from Logged_In import login
from random_account_maker import dictionary_handler, dictionary_updater
from create_account import account_creator, account_creation
from sign_in import account_detail, deposit, withdraw, update_pin, check_statement
amount = 0
main_menu_options = ['Create Account', 'Checkin', 'Exit']
sub_options_menu = ['Account Detail', 'Deposit', 'Withdraw', 'Update Pin', 'Check Statement', 'Logging Out']
print("Welcome to Random Bank")

while True:
    try:
        for option_num, options in enumerate(main_menu_options):
            print(f"Enter {option_num} To {options}")
        choice = input("\n")

        if choice == '0':
            new_user = account_creation(account_creator())
            dictionary_updater(dictionary_handler(), new_user)
            dicts = dictionary_handler()
            current_account_num = tuple(dicts.keys())[-1]
            username = dicts[current_account_num]["username"]
            print(f"Now You can login, your username is {username} and your account num is: {current_account_num}")

        elif choice == '1':
            acc_num = (login(dictionary_handler()))[1]  # returns account number
            if acc_num[0]:  # returns True
                while True:
                    for sub_option_num, sub_options in enumerate(sub_options_menu):
                        print(f"Enter {sub_option_num} For {sub_options}")
                    action = input()
                    if action == '0':
                        details = account_detail(acc_num, dictionary_handler())
                        next_value = iter(details)
                        print(
                            f"Branch Name: {next(next_value)}\nAccount Number: {next(next_value)}\nName: {next(next_value)}\n*********")
                        print(
                            f"Currency: {next(next_value)}\nAccount Opening Date: {next(next_value)}\nLast Transaction: {next(next_value)}\n*********")
                        print(
                            f"Your Current Balance: {next(next_value)}\nCurrent Status of your account: {next(next_value)}\n")
                    elif action == '1':

                        count = 0
                        while count != 3:
                            try:
                                amount = input("Enter amount to deposit, You can only deposit multiples of 500\n")
                                value = int(amount)

                                if value % 500 != 0:
                                    raise ValueError
                                break
                            except ValueError:
                                print("Invalid input")
                            if count == 2:
                                print("Sorry Something went wrong")
                                break
                            count += 1
                        current_dictionary = dictionary_handler()
                        deposit(acc_num, current_dictionary, amount)
                        print(f"This is your current balance amount: {current_dictionary[acc_num]['acc_details']['balance_amount']}")
                    elif action == '2':
                        count = 0
                        while count != 3:
                            try:
                                amount = input("Enter amount to withdraw, You can only withdraw multiples of 500\n")
                                value = int(amount)

                                if value % 500 != 0:
                                    raise ValueError
                                break
                            except ValueError:
                                print("Invalid input")
                            if count == 2:
                                print("Sorry Something went wrong")
                                break
                            count += 1
                        current_dictionary = dictionary_handler()
                        balance = withdraw(acc_num, current_dictionary, amount)
                        print(balance)
                    elif action == '3':
                        count = 0
                        while count != 3:
                            if count == 2:
                                print("Sorry Something went wrong")
                            pin = input("Enter Pin\n")
                            try:
                                pin_str = pin
                                pin = int(pin)
                                if len(pin_str) > 4:
                                    raise Exception("Length can not exceed 4 numeric digits")
                                break
                            except ValueError as e:
                                print("Enter Integers Only")
                            except Exception as e:
                                print(e)
                            count += 1
                        update_pin(acc_num, dictionary_handler(), pin_str)
                    elif action == '4':
                        check_statement(acc_num, dictionary_handler())
                    elif action == '5':
                        print("Logging You Out, Hope to see you next time, Allah Hafiz")
                        break

        elif choice == '2':
            print("Allah Hafiz See You Later!")
            break
        else:
            raise ValueError("Enter Valid Value")
    except TypeError as e:
        pass  # skipping this error as if pi is invalid None Type is returned
    except Exception as e:
        print(e)

