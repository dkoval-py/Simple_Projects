import sys

while True:
	try:
		a = float(input('Enter first number: '))
		b = float(input('Enter second number: '))
		print(a ** 2 / b)
	except ValueError:
		print('Error: ', sys.exc_info()[1])
	except ZeroDivisionError:
		print('Error:', sys.exc_info()[1])
	else:
		exit()