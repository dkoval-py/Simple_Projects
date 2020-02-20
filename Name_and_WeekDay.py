# Modules for definitioning the currect day
from datetime import date
import calendar
# Modules for using the colorful text 
from colorama import init
from colorama import Fore
# For Windows it's necessary to call the init()
init()

# Assigning the current date to the variable
current_date = date.today()

# print(current_date)
# print(current_date.weekday())

# Stored the week day in the variable
week_day = calendar.day_name[current_date.weekday()]

print(Fore.GREEN)
user_name = input("Hey, what's your name? ")

print(Fore.RED)
print('"Good day {0}! {1} is a perfect day to learn some python!!!"'.format(user_name, week_day))