# Generate unique array
import random

'''
On input we are getting the array lenth
'''
def unique_array(array_lenth):
	# The empty array and iterator 
	my_array = []
	i = 0

	while i < array_lenth:
		# The variable which shows if there is the equal numbers in the array
		is_number_in_array = False
		
		# Temporary value for new random number
		temp_value = int(random.uniform(0, array_lenth))

		# Cycle for checking if there are equal numbers in the array 
		for j in range(0, i):
			''' 
			If there is equal number in the array, we set bool value to true
			and finish the cycle 
			'''
			if my_array[j] == temp_value:
				is_number_in_array = True
				break
		'''
		If there are no equals numbers we add the random number
		from temp_value to our array.
		And rise the iterator
		'''
		if is_number_in_array == False:
			my_array.append(temp_value)
			i += 1

	return my_array 

print(unique_array(20))
