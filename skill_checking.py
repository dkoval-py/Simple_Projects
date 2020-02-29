from colorama import init
from colorama import Fore, Style
init()

# Function for giving the goods to users
def human_fruits(goods, hum):
	fruits = list(goods.keys())

	add_fruits = list(map(lambda x, y: x + ' - ' + y, hum, fruits))
	
	print('Gave fruits to users:')
	for i in add_fruits:
		print('\t', i)

# Function for checking if there is such good
def is_On_basket(user_goods, goods):
	for i in goods.keys():
		is_there = True

		if user_goods == i:
			is_there = True
			break
		else: 
			is_there = False
	
	if is_there == True:
		print('\t', user_goods, ' - there is such fruit')
	else:
		print('\t', user_goods, ' - there is no such fruit')


# The function for counting the prices
def Total_Goods_Price(goods, price):
	quentity = list(goods.values())
	price_list = list(price.values())

	total_price_list = list(i * j for i, j in zip(quentity, price_list))

	print(Fore.GREEN)
	print('\nThe price for each fruits is:', total_price_list)

	total_price = 0
	for x in total_price_list:
		total_price += x

	print('The total price for all fruits is:', total_price)
	

# Goods and there quantity
goods = {
	'apple' : 1,
 	'orange' : 2, 
 	'banana' : 3, 
}


# The price of goods
price = {
	'apple' : 5,
 	'orange' : 12, 
 	'banana' : 33, 
}

print(Fore.GREEN, Style.BRIGHT)
# Print out all goods: 
print('\nAll goods: ', list(goods.keys()))


# Print out goods and there quantity
print(Fore.YELLOW)
print('\nThe quantity of goods: ')
for i, x in goods.items():
	print('\t', i, '-', x)


print(Fore.GREEN)
# Check if there is such good which user has entered
user_goods = str(input('\nYou can check which goods are: '))
is_On_basket(user_goods, goods)


print(Fore.YELLOW)
# Enter list of people
hum = set(map(str, input('\nEnter Users: ').split()))


human_fruits(goods, hum)

Total_Goods_Price(goods, price)