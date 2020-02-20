# Quadratic eqations: ax^2 + bx + c = 0  ----  V1.0
import math
print('The type of equation is: \n\tax^2 + bx + c = 0')
print('\nEnter your values.')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

Discriminant = b ** 2 - 4 * a * c

if Discriminant < 0:
	print('There are no roots in this equation')
elif Discriminant == 0:
	x = -b / (2 * a)
	print('There is one root: x = ', x)
elif Discriminant > 0:
	x1 = (-b + math.sqrt(Discriminant)) / (2 * a)
	x2 = (-b - math.sqrt(Discriminant)) / (2 * a)
	print('There are two roots: ')
	print('\tx1 =', x1)
	print('\tx2 =', x2) 
