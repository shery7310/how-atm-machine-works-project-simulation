import time
from random_account_maker import dictionary_writer, dictionary_handler

count = 0


def login(dictionary):
    global count
    try:
        acc_num = input("Enter Valid Account Number\n")
        if acc_num in dictionary:
            if dictionary[acc_num]['status'] == "Active":
                while count != 3:
                    verify = verify_pin(dictionary, acc_num)
                    if verify:
                        if count == 0:
                            return True, acc_num
                    elif verify:
                        if count == 1:
                            return True, acc_num
                    elif count == 2:
                        dictionary[acc_num]['status'] = "Blocked"
                        print("Sorry Your Account Has been Blocked, as you have been entering an invalid pin number")
                        dictionary_writer(dictionary)
                        return False
                    count += 1
            else:
                raise ValueError("Sorry this account has been blocked, Contact Helpline")
        else:
            raise ValueError("Account number doesn't exist")
    except ValueError as e:
        print(e)


def verify_pin(handler, acc_num):
    global count
    dictionary = handler
    pin = input("Enter Your Pin:\n")
    if dictionary[acc_num]['pin_code'] == pin:
        time.sleep(2)
        print("Logging You In.....")
        return True
    else:
        return None
