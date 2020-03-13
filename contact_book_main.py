# -*- coding: utf-8 -*-
from contact_book_class import * # Імпортуємо клас з файла contact_book_class.py

# Змінна для перевірки чи хоче користувач продовжувати працювати з програмою
is_continue = True

while is_continue == True: 
	check_value = True # Зміна, для циклу в якому ловимо помилку ValueError
	check_number = True # Змінна, для циклу в якому перевіряємо коректність вибору меню

	while check_value == True:
		try:
			print('''\nChoose the action: 
				1 - Add new contact
				2 - Search in contact book
				3 - Delete from contact book
				''')
			action = int(input('>>> ')) # Обираємо дію

			if action == 1:
				while check_number == True:
					try:
						# Кількість новиї записів
						contact_quantity = int(input('Contact quantity: '))

						if contact_quantity <= 0:
							print('!!!Error!!! Incorrect type of value.')
							continue

					except ValueError:
						print('!!!Error!!! Incorrect type of value.')
						continue
					else:
						check_number = False

				
				new_object = Contact_book(contact_quantity) # Створюємо об'єкт класа
				new_object.Add_new_contact() # Викликаємо метод щоб додати контакт
			
			'''Блоки з ключами 2 та 3 не працюють,
			ящо перед цим не викликався блок з ключем 1
			'''
			elif action == 2:  
				new_object.Find_in_book() # Викликаємо метод для пошуку

			elif action == 3:
				new_object.Delete_form_book() # Метод для видалення
			else:
				print('\t\t!!!Error!!! Incorrect type of value.')
				continue

		except ValueError:
			print('\t\t!!!Error!!! Incorrect type of value.')
			continue
		else:
			check_value = False

	# Локальна зміна на перевірку чи буде продовжувати працювати
	check_continue = True  
	
	while check_continue == True:
		cont = input('Do you want to continue (Y/n): ')
		if cont == 'n' or cont == 'N':
			is_continue = False
			check_continue = False
		elif cont == 'Y' or cont == 'y':
			check_continue = False
		else:
			print('!!!Incorrect answer')
