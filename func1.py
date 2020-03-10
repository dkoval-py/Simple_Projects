def make_country(param):
	country_capital = {}

	for i, j in param.items():
		country_capital[i] = j

	return country_capital


entered_dict = {}

count = int(input('Enter the count of countries: '))

while count > 0:
	entered_dict[input('Enter a country: ')] = input('Enter a capital: ')

	count -= 1

print(make_country(entered_dict))