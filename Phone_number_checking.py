from colorama import init
from colorama import Fore, Style
init()

print(Fore.RED, Style.BRIGHT)
print('We\'re serving only Ukraininan customers!!!  ', end = '')
print('(It means that your number\'s international code has to be +380)')

print(Style.RESET_ALL)
print('\tPlease, enter your valid phone number: +380', end = '')
customer_phone = input()

if len(customer_phone) == 9:
	print(Fore.GREEN, Style.BRIGHT)
	print('You\'re phone number is (+380)-', end = '')
	print(customer_phone[0:2], '-', customer_phone[2:4], '-', sep = '' ,end = '')
	print(customer_phone[4:6], '-', customer_phone[6:], sep = '')
	print('Thanks, we\'ll contact you soon')
else:
	print(Fore.RED, Style.BRIGHT)
	print('!!!ERROR: You\'ve entered wrong number, please check again')