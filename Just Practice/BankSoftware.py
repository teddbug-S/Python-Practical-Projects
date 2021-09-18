import datetime
import json
from random import shuffle
from sys import exit

from inputimeout import inputimeout, TimeoutOccurred

# creating a date time object
current_date = datetime.datetime.now()


# defining my authenticators

# Creating a class for the auths
class LoginAuths:
    """
    This class contains all the necessary authenticators to make sure your login or sign up system is stable.
    This also helps to make sure you don't store wrong values to your database."""

    # this function instantiates the class object
    # with all the necessary parameters passed.
    def __init__(self, /, user_age, f_name, l_name, user_pin, user_confirm_pin):
        self.age = user_age
        self.f_name = f_name
        self.l_name = l_name
        self.pin = user_pin
        self.confirm_pin = user_confirm_pin

    # age authenticator, to make sure user is a teen
    def ageAuthenticator(self):
        """Takes in the age of user and make sure it's above 12 and below 166
           It returns True if the condition is met, else False."""

        if 15 < int(self.age) <= 164:
            return True
        else:
            return False

    # check name to make sure it doesn't contain any other characters apart form the alphabets
    def nameAuthenticator(self):
        """This method of the class checks the f_name and l_name if it does not contain any foreign characters
           such as space, symbols etc. Returns True if it follows the condition else, False."""

        if self.f_name.isalpha() and self.l_name.isalpha():
            return True
        else:
            return False

    # to make sure passwords match
    def pinAuthenticator(self):
        """This method compares the first_password and confirm_password to see if they match
           and are more than or equal to 8 characters.
           Returns True if they do else, False."""

        if self.pin == self.confirm_pin and len(self.pin) == 4:
            return True
        elif len(self.pin) < 4:
            return 0
        else:
            return False


# trying to make the necessary directories

print("{:-^167}".format('Welcome To UniQue Bank'))
print(current_date.strftime("%A, %d of %B %Y\n"))
print("[1]--Sign Up\t[2]--Log In\n[3]--Exit".expandtabs(8))
try:
    while True:
        chances = 3
        option = input('\nEnter option: ')

        if option == '2':
            try:  # let's try reading the file or database
                account_number = int(inputimeout(prompt="Enter account number: ", timeout=15))
                account_pin = int(inputimeout(prompt='Enter PIN: ', timeout=15))

                account_nums = []
                account_pins = []
                full_user_info = {}
                with open(r'users.json', 'r') as user_data:
                    user_info = json.load(user_data)  # storing user data into the user info variable as a list of dicts
                    for each_user in user_info:
                        account_nums.append(each_user['Account Number'])
                        account_pins.append(each_user['PIN'])
                        for key, value in each_user.items():
                            full_user_info[key] = value

                    if account_number in account_nums and account_pin in account_pins:
                        print('\nWelcome Back {FirstName},'.format(**full_user_info))
                        print('\n!{:-^45}!\n'.format('Your UniQue Bank Dashboard'))
                        print('Current balance: {Amount}\nLast Deposit made: {Time}'.format(**full_user_info))

                    elif account_number in account_nums:
                        print('Incorrect PIN')

                    elif account_pin in account_pins:
                        print('Incorrect Account Number.')

                    elif account_pin is None and account_number is None:
                        print("Sorry you did not enter anything try again.")

                    else:
                        print("\nWe don't have any details like that in our database enter 1 to register.")
            except (FileNotFoundError, FileExistsError, json.JSONDecodeError):
                print("\nOops! We currently don't have any customers yet, be our first customer and earn N5,000.")

            except (TypeError, NameError, ValueError):
                print("You entered a wrong value.")
            except TimeoutOccurred:
                print('Time limit exceeded. Try again')
                chances -= 1

        elif option == '1':
            try:
                f_name = input('First Name: ').strip()
                l_name = input('Last Name: ').strip()
                age = input('Age: ').strip()
                pin = input('Choose PIN: ').strip()
                confirm_pin = input('Re-enter PIN: ').strip()

                amount_given = 5000

                # Now let's authenticate these inputs to ensure we save the right data into our database
                myAuths = LoginAuths(
                    f_name=f_name,
                    l_name=l_name,
                    user_age=age,
                    user_pin=pin,
                    user_confirm_pin=confirm_pin,
                )

                # Now let's apply these methods and see
                check_name = myAuths.nameAuthenticator()
                check_age = myAuths.ageAuthenticator()
                check_pin = myAuths.pinAuthenticator()

                # opening the db to make sure account number is unique

                # Generating an account number
                def num_generator():
                    gen_list = [i for i in range(10)]
                    shuffle(gen_list)
                    gen_str = ""
                    for i in gen_list:
                        gen_str += str(i)
                    return gen_str


                account_numbers = []
                try:
                    with open(r'users.json', 'r') as user_data:
                        user_info = json.load(
                            user_data)  # storing user data into the user info variable as a list of dicts
                        for each_user in user_info:
                            account_numbers.append(each_user['Account Number'])

                    account_number = int(num_generator())
                    if account_number not in account_numbers:
                        account_number = int(num_generator())
                    else:
                        account_number = int(num_generator())
                except (FileNotFoundError, json.JSONDecodeError):
                    account_number = int(num_generator())

                if not check_age:
                    print('Oops you must be above 12 years old.')
                elif not check_name:
                    print('Please enter your legal first and last names.')
                elif not check_pin:
                    print("Please the PINs you entered do not match.")
                elif check_pin == 0:
                    print("PIN must be a 4-digit number.")
                else:
                    # else meaning if  all are set then let's do some preview of the data we got from the user
                    print('Preview:')
                    print('--First Name: {}\n--Last Name: {}\n--Age: {}\n--New Account Number: {}\n--Your PIN: {}\n\n'.
                          format(f_name, l_name, age, account_number, pin))

                    # asking whether to proceed or not
                    print("Enter {!r} to sign up, {!r} to discard.".format("Yes", "No"))
                    save_option = input("Do you wish to continue: ")
                    if save_option == "Yes" or save_option == "yes":
                        main_data_container = []
                        data_gathered = {
                            'FirstName': f_name,
                            "LastName": l_name,
                            "Age": age,
                            "PIN": int(pin),
                            "Amount": "N{:.2f}".format(amount_given),
                            "Time": current_date.strftime("%A, %d of %B %Y"),
                            "Account Number": account_number
                        }

                        try:
                            # we do that by opening it first
                            with open(r"users.json", "r") as user_account_data:
                                # loading from json to python also same as reading it to store the current items init
                                # first
                                account_data = json.load(user_account_data)
                                # Let's add new user's to the old ones
                                account_data.append(data_gathered)
                                # now let's write what we have to the file for storing but we need to open it in
                                # write mode, I could just open it in write mode but in the first with block but if I
                                # do it will truncate the file thus losing the data we first stored.
                                with open(r"users.json", "w") as user_account_data2:
                                    # writing to it
                                    json.dump(account_data, user_account_data2, indent=4, sort_keys=True)

                        # But what if we did not succeed reading the file due to some exceptions?
                        # Let's create a new file then and store the data in it
                        except (FileNotFoundError, json.JSONDecodeError, NameError, ValueError, TypeError):
                            pass
                            # Let's create a new file if it's not already in existence or
                            # something has occurred and the file got corrupt
                            with open(r"users.json", "w+") as user_account_data:
                                # as the JSON parser requires, "a list containing a comma separated dict values"
                                # let's append the dict value to the main_data_container list and save.
                                main_data_container.append(data_gathered)
                                json.dump(main_data_container, user_account_data, indent=True, sort_keys=True)
                            # giving the user a feedback.
                        print("\nCongratulations, registered successfully.")

                        # if user maybe made a mistake or doesn't want to save the data, let's let user know it wasn't
                        # saved.
                    else:
                        print("\nData you entered was not saved.")
            except (TypeError, NameError, ValueError):
                print('Some error occurred please check your inputs.')

            except (FileNotFoundError, FileExistsError, json.JSONDecodeError):
                pass

        elif option == '3':
            exit("{:-^100}".format("Good Bye "))

        else:
            print('Invalid option.')

except (ModuleNotFoundError, ImportError):
    print('Oops! Please install the {!r} module via the command {!r}'.format('inputimeout', 'pip install inputimeout'))
