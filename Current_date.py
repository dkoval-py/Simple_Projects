import datetime
def Current_date():

	d = datetime.datetime.today()

	print('Year:', d.year)
	print('Month:', d.month)
	print('Day:', d.day)
	print('Hour:', d.hour)
	print('Minute:', d.minute)

Current_date()