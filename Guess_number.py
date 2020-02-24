# Guess number
import random

guess = int(random.uniform(0, 11))
is_right = False

while is_right == False:
	user_number = int(input('Please enter the number: '))

	if user_number == guess:
		print('You\'re rigth! My number is', user_number)
		is_right = True
	elif user_number < guess:
		print('You\'re wrong, my number is a little bit heigher')
	elif user_number > guess:
		print('You\'re wrong, my number is less')