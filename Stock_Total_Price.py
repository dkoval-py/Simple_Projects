def Total_Price(stock, prices):
	stock_list = list(stock.values())
	prices_list = list(prices.values())

	result_list = []

	result_list = [i * j for i, j in zip(stock_list, prices_list)]
 
	total = 0
	for x in result_list:
		total += x

	return total


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print('The total price of stock is', Total_Price(stock, prices))