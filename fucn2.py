def make_operation(operation, first, *args):
	return_value = first

	if operation == '+':
		for i in args:
			return_value += i
		return return_value
	elif operation == '-':
		for i in args:
			return_value -= i
		return return_value
	elif operation == '*':
		for i in args:
			return_value *= i
		return return_value
	else:
		print('Incorrect operation')

print(make_operation('-', 3, 4, -10, -20))