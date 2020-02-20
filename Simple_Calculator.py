# Simple_calculator V1.0
from colorama import init
from colorama import Fore
init()

print(Fore.GREEN)
first_number = float(input('Please enter first number: '))

# Available mathematical operations: +, -, /, *, **, |x|
print('Choose the number of the action:')
print('\t1 - Addition;\n\t2 - Subraction;\n\t3 - Division;')
print('\t4 - Multiplacation;\n\t5 - Exponent;\n\t6 - Modulus; ')

action = int(input())
if action == 6:
	print(Fore.YELLOW)
	print('Result', abs(first_number))
	exit()
if action <= 0 or action > 6:
	print(Fore.RED)
	print('!!!ERROR: You\'ve chosen incorrect action')

print(Fore.GREEN)
second_number = float(input('Pleae enter second number: '))

print(Fore.YELLOW)
if action == 1:
	print('Result: ', first_number + second_number)
elif action == 2:
	print('Result: ', first_number - second_number)
elif action == 3:
	if second_number == 0:
		print(Fore.RED)
		print('!!!ERROR: You can\'t devision to null')
	else:
		print(Fore.YELLOW)
		print('Result: ', first_number / second_number)
elif action == 4:
	print(Fore.RED)
	print('Result: ', first_number * second_number)
elif action == 5:
	print('Result: ', first_number ** second_number)
