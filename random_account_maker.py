import random
import calendar
import datetime
import ast

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
random_names = ['Mehfuz Ali', 'Barkat Iqbal', 'Sohail Rauf', 'Rizwan Khan', 'Jamaluddin Butt', 'Rashid Minhas',
                'Nadir Shah', 'Jamshed Ahmed', 'Sajjad Hussain', 'Khalid Mehmood', 'Naveed Akhtar', 'Ali Adil',
                'Ayra Fatima', 'Waqar Younus', 'Jamil Ahmed', 'Zafar Iqbal', 'Eman Hassan', 'Nadir Ali', 'Kamran Akmal',
                'Imtiaz Khan', 'Shahid Afridi', 'Mohsin Khan', 'Rehan Siddiqui', 'Imran Abbas', 'Umer Farooq',
                'Bilal Qureshi',
                'Usman Ghani', 'Haris Sohail', 'Danish Nawaz', 'Hasnain Raza', 'Faheem Ashraf', "Abdul Mannan",
                'Asif Ali',
                'Hussain Talat', 'Mohammad Hafeez', 'Shahrukh Khan', 'Ahmed Shehzad', 'Mubasshar Khan', 'Mohammad Amir',
                'Asif Hussain', 'Mudassar Ali', 'Sarfaraz Ahmed', 'Azhar Ali', 'Asad Shafiq', 'Babar Azam',
                'Fakhar Zaman',
                'Shoaib Akhtar', 'Ayesha Khan', 'Shehryar Zulfiqar', 'Maleeha Lodhi', 'Harrib Abdul Rafey',
                'Nabeel Asif',
                'Abeera Rafique', 'Taha Shabbir', 'Waleed Bashir', 'Saira Bano', 'Saima Rajput']
sample_years = [2018, 2019, 2020, 2021, 2022, 2017, 2016, 2015, 2014, 2013,
                2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003,
                2002, 2001, 2000]
cell_numbers = [
    '03155032294', '03383059103', '03162024687', '03321064839', '03415092378',
    '03465092837', '03154092173', '03352048631', '03146027549', '03342079351',
    '03115048952', '03553076492', '03212086437', '03243029541', '03438092562',
    '03137091852', '03362054761', '03456092173', '03143048596', '03402095478',
    '03231028465', '03163059482', '03488051964', '03353062951', '03242037569',
    '03476029583', '03122095478', '03522039647', '03447032965', '03362029501',
    '03483029274', '03458092651', '03251093857', '03265091837', '03429085631',
    '03273029658', '03182093457', '03192083759', '03174029568', '03215076923',
    '03399087643', '03136025849', '03153076952', '03142068437', '03367092581',
    '03286037452', '03555029183', '03498027653', '03482073655', '03227046839',
]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
address_list = [
    'Flat#5, St 10, Phase 5, DHA, Lahore',
    'Flat#16, St 14, Cavalry Ground, Lahore',
    'Flat#10, St 5, Johar Town, Lahore',
    'Flat#20, St 2, Wapda Town, Lahore',
    'Flat#7, St 13, Gulberg 3, Lahore',
    'Flat#19, St 1, Township, Lahore',
    'Flat#13, St 8, Faisal Town, Lahore',
    'Flat#2, St 3, Askari 14, Rawalpindi',
    'Flat#7, St 5, Bahria Town, Phase 8, Rawalpindi',
    'Flat#31, St 2, Satellite Town, Rawalpindi',
    'Flat#9, St 4, Chandni Chowk, Rawalpindi',
    'Flat#22, St 5, Sadiqabad, Rawalpindi',
    'Flat#15, St 2, Al-Haram, G-10, Islamabad',
    'Flat#27, St 7, E-11, Islamabad',
    'Flat#1, St 4, F-8, Islamabad',
    'Flat#7, St 2, F-10, Islamabad',
    'Flat#31, St 5, G-7, Islamabad',
    'Flat#20, St 9, F-6, Islamabad',
    'Flat#12, St 8, I-10, Islamabad',
    'Flat#18, St 3, G-6, Islamabad',
    'Plot#9, St 17, North Nazimabad, Karachi',
    'Plot#23, St 1, North Karachi, Karachi',
    'Plot#7, St 13, Nazimabad, Karachi',
    'Plot#19, St 5, Gulshan-e-Iqbal, Karachi',
    'Plot#31, St 2, Federal B Area, Karachi',
    'H#22, St 8, Malir, Karachi',
    'H#15, St 11, Landhi, Karachi',
    'H#10, St 7, Korangi, Karachi',
    'H#2, St 5, Clifton, Karachi',
    'H#14, St 2, Saddar, Karachi',
    'H#25, St 4, Cavalry Ground, Gujranwala',
    "H#18, St 7, People's Colony, Gujranwala",
    'H#39, St 13, Sharif Pura, Sialkot',
    'H#12, St 10, Paris Road, Sialkot',
    'H#7, St 5, Jinnah Road, Jhelum',
    'H#31, St 8, Saddar Bazar, Jhelum',
    'H#9, St 3, Satellite Town, Gujrat',
    'H#21, St 15, Urdu Bazar, Gujrat',
    'H#25, St 13, Timergara Road, Dir',
    'H#19, St 9, Baloch Pura, Bhera',
    'H#16, St 11, Jinnah Bagh, Sheikhupura',
    'Flat #3, St 2, Satellite Town, Sargodha',
    'Plot #15, St 10, Cantt Area, Sargodha',
    'Flat #12, St 7, Jinnah Town, Sahiwal',
    'Plot #8, St 4, Green Town, Sahiwal',
    'Flat #20, St 16, Gawal Mandi, Faisalabad',
    'Plot #27, Engineers St 2, Akbar Chowk, Faisalabad',
    'H#3, Engineers St, DHA Phasee 5, Lahore'
    'H#10, St 12, Korangi, Karachi',
    'Plot#19, St 5, Gulshan-e-Iqbal, Karachi'
    'H#213, St 15, Urdu Bazar, Lahore',
    'H#2, Shadman Rd, Clifton, Karachi',
]
random_balance = random.sample(range(2000, 10000), 50)
usernames = {'MehfuzAli221': 'Mehfuz Ali',
             'BarkatIqbal3192': 'Barkat Iqbal',
             'SohailRauf8593': 'Sohail Rauf',
             'RizwanKhan4359': 'Rizwan Khan',
             'JamaluddinButt2938': 'Jamaluddin Butt',
             'RashidMinhas8301': 'Rashid Minhas',
             'NadirShah1029': 'Nadir Shah',
             'JamshedAhmed2832': 'Jamshed Ahmed',
             'SajjadHussain3921': 'Sajjad Hussain',
             'KhalidMehmood2910': 'Khalid Mehmood',
             'NaveedAkhtar8310': 'Naveed Akhtar',
             'AliAdil2901': 'Ali Adil',
             'AyraFatima3762': 'Ayra Fatima',
             'WaqarYounus2910': 'Waqar Younus',
             'JamilAhmed2832': 'Jamil Ahmed',
             'ZafarIqbal3921': 'Zafar Iqbal',
             'EmanHassan2901': 'Eman Hassan',
             'NadirAli8310': 'Nadir Ali',
             'KamranAkmal3029': 'Kamran Akmal',
             'ImtiazKhan5820': 'Imtiaz Khan',
             'ShahidAfridi4810': 'Shahid Afridi',
             'MohsinKhan5932': 'Mohsin Khan',
             'RehanSiddiqui4382': 'Rehan Siddiqui',
             'ImranAbbas1234': 'Imran Abbas',
             'UmerFarooq2845': 'Umer Farooq',
             'BilalQureshi3821': 'Bilal Qureshi',
             'UsmanGhani4930': 'Usman Ghani',
             'HarisSohail5839': 'Haris Sohail',
             'DanishNawaz4958': 'Danish Nawaz',
             'HasnainRaza3048': 'Hasnain Raza',
             'FaheemAshraf3029': 'Faheem Ashraf',
             'AbdulMannan4839': 'Abdul Mannan',
             'AsifAli4958': 'Asif Ali',
             'HussainTalat1234': 'Hussain Talat',
             'MohammadHafeez5839': 'Mohammad Hafeez',
             'ShahrukhKhan1234': 'Shahrukh Khan',
             'AhmedShehzad4815': 'Ahmed Shehzad',
             'MubassharKhan3915': 'Mubasshar Khan',
             'MohammadAmir4957': 'Mohammad Amir',
             'AsifHussain1234': 'Asif Hussain',
             'MudassarAli8301': 'Mudassar Ali',
             'SarfarazAhmed3921': 'Sarfaraz Ahmed',
             'AzharAli4957': 'Azhar Ali',
             'AsadShafiq3809': 'Asad Shafiq',
             'BabarAzam2910': 'Babar Azam',
             'FakharZaman8301': 'Fakhar Zaman',
             'ShoaibAkhtar1234': 'Shoaib Akhtar',
             'AyeshaKhan3921': 'Ayesha Khan',
             'ShehryarZulfiqar4957': 'Shehryar Zulfiqar',
             'MaleehaLodhi3809': 'Maleeha Lodhi',
             'HarribAbdulRafey2910': 'Harrib Abdul Rafey',
             'NabeelAsif8301': 'Nabeel Asif',
             'AbeeraRafique1234': 'Abeera Rafique',
             'TahaShabbir3921': 'Taha Shabbir',
             'WaleedBashir4957': 'Waleed Bashir',
             'SairaBano3809': 'Saira Bano',
             'SaimaRajput2910': 'Saima Rajput'
             }

count = 0
users = {}


def random_pins():
    """ Creates random pins"""
    pin = random.randint(1000, 9999)
    return str(pin)


def dictionary_handler():
    """ This will always provide the dictionary in read mode, replaces users = """
    try:
        with open("Customers.txt") as read_customers:
            users_string = read_customers.read()
            users_string = users_string.replace("users = ", "")
        users_dict = ast.literal_eval(users_string)
        return users_dict
    except FileNotFoundError as e:
        print("Sorry the link is down please try again in a while")
    except SyntaxError as e:
        print("Sorry there seems to be a problem with Your data, try later", e)
    except Exception as e:
        print("Something went wrong", e)


def dictionary_writer(handler):  # expects an evaluated dictionary
    """ This will used to write the dictionary to the txt file,
    will take dictionary from dictionary_handler function, appends users = at the start of the dictionary"""
    users_dict = handler
    users_dict_str = str(users_dict)
    users_dict_str = "".join(["users = ", users_dict_str])
    try:
        with open("Customers.txt", "w") as write_customers:
            write_customers.write(users_dict_str)
    except FileNotFoundError as e:
        Exception("Sorry the link is down please try again in a while", e)
    except AttributeError as e:
        Exception("Sorry the link is down please try again in a while")
    except Exception as e:
        print(e)


def dictionary_updater(handler, new_user):
    """ Adds newly created user to the dictionary and the appends users = to the start"""
    users_dict = handler
    users_dict.update(new_user)
    users_dict_str = str(users_dict)
    users_dict_str = "".join(["users = ", users_dict_str])
    try:
        with open("Customers.txt", "w") as write_customers:
            write_customers.write(users_dict_str)
    except FileNotFoundError:
        Exception("Sorry the link is down please try again in a while")
    except AttributeError:
        Exception("Sorry the link is down please try again in a while")
    except Exception as e:
        print(e)


def account_number_creator(branch_code):
    """ Creates A random account number taking branch code as an argument,
    also fetches branch name from branch_codes dictionary"""
    num = str(random.randint(1000_0000_00, 9999_9999_99))
    account_number = branch_code + num
    branch_name = branch_codes[branch_code]
    return account_number, branch_name


def random_date():
    """ Returns a tuple of random date, first format for account_creation_date
    and the other one for statement"""
    while True:
        year = random.choice(sample_years)
        month = random.randint(1, 12)
        month_days = calendar.monthrange(year, month)[1]  # number of days in a month
        day = random.randint(1, month_days)  # random day

        date = datetime.date(year, month, day)
        weekday = date.weekday()  # we don't want saturday and sunday

        if weekday >= 0 and weekday <= 4:  # if weekday is between range break and return
            break

    time = datetime.time(random.randint(9, 12), random.randint(0, 59))  # 24 hr
    current_date = datetime.datetime.combine(date, time)

    return current_date.strftime('%A, %d-%h-%Y, %I:%M %p'), current_date.strftime(
        '%d-%h-%Y, %I:%M %p')  # Thursday, 09-Sep-2010, 09:45 AM


def random_account_number_creator(branch_code, current):
    """ Creates an entirely random user, with random details to populate txt file"""
    num = str(random.randint(1000_0000_00, 9999_9999_99))
    account_number = branch_code + num
    full_date = random_date()
    date = full_date[0]
    date2 = full_date[1]
    usernames_names = usernames.items()
    username = tuple(usernames_names)[current][0]
    name = tuple(usernames_names)[current][1]
    status = "Active"
    balance_amount = random.choice(random_balance)
    currency = "PKR"
    cell_number = cell_numbers[current]
    branch_name = branch_codes[branch_code]
    pin_code = random_pins()
    users_txt = {account_number: {"name": name, "username": username, 'branch_code': branch_code,
                       "branch_name": branch_name, "pin_code": pin_code,
                       "status": status, "account_creation_date": date, "cell_number": cell_number,
                       "acc_details": {'statement': {f'+{balance_amount}': date2},
                                       "balance_amount": f'{balance_amount}', "currency": currency,
                                       }
                       }
                 }
    return users_txt


def dict_updater():
    """ Creates 50 Random Users using random_date, random_account_number_creator
    and the writes to customers.txt in w mode, so BE CAREFUL running it"""
    global count, users
    while count != 50:
        user = random_account_number_creator(random.choice(tuple(branch_codes.keys())), count)
        users.update(user)
        count += 1
    users_txt = str(users)
    users_txt = "".join(["users = ", users_txt])

    with open("Customers.txt", "w") as file:
        file.write(users_txt)
