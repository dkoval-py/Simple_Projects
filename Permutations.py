# Permutatuions
import itertools

user_string = input('Enter your string: ')

for i in itertools.permutations(user_string):
	print(i)