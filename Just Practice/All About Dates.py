from os import name, system
from datetime import datetime
from textwrap import fill
from math import ceil
from collections import namedtuple

from dates import data_gathered

# Practicing with the datetime module in python so I thought of having a little fun
# Enter your name on te first line of input, on the second line enter your birth date
# in this format YYYY/MM/DD it should be in that same format please.

def clear_screen():
    system('clear')

def calculate_dates(date):
    """ Peforms calculations with the date user provided. """
    Date = namedtuple('Date', ['days_lived', 'months_lived', 'age', 'month', 'actual_age', 'leaps'])
    date = datetime(*[int(i) for i in date.split('/')])
    c_date = datetime.now()
    time_delta = c_date - date
    leaps = [str(year) for year in range(date.year, c_date.year+1) \
        if year%4==0 or year%400==0 and year%100==0]

    return Date(
        days_lived=time_delta.days,
        age=time_delta.days//365,
        actual_age=time_delta.days/365,
        months_lived=time_delta.days//12,
        leaps=leaps,
        month=datetime.strftime(date, "%B")
        )

def get_propeties(month):
    """ Returns the user's zodiac, traits and common personalities. """
    data = data_gathered.get(month)
    Props = namedtuple('Props', ['traits', 'zodiac', 'people'])
    return Props(
        traits=data['Traits'],
        zodiac=data['Zodiac'],
        people=data['People']
    )

def get_message(name, date):
    """ Generates the message with all the data. """
    # get the date data
    date = calculate_dates(date)
    # get user properties
    props = get_propeties(date.month)
    # define template
    template = f"""
    Hello {name}, here are some few facts about you!
    You're {date.age} years old, but more accurately {date.actual_age:.2f} years old
    that's approximately {round(date.actual_age)} years old.
    You've been on earth for about {date.days_lived} days, {date.months_lived} months,
    lived {len(date.leaps)} leap years which are {', '.join(date.leaps)}.
    You are the {props.traits[0].lower()} type, most people love that about you
    but you can also be {props.traits[1].lower()} sometimes, you were born 
    under the {' or '.join(props.zodiac)} star which is cool.
    There are quite a few famous personalities you share birth months with,
    they are {' and '.join(props.people)} and you're likely going to great 
    like them.
    """
    return template


if __name__ == '__main__':
    name = input("Enter your name: ").title()
    print("Enter your birthdate in the format YYYY/MM/DD.")
    date = input("Birth date: ")
    message = get_message(name, date)
    clear_screen()
    print("\n\t\t\t!{0:-^30}!\n\n".format("It's All About Dates"))
    print(f"\t{message}\n\n\n\n")
