# -*- coding: utf-8 -*-
import json


class Contact_book():
	'''Клас для контанків (ім'я, фамілія, номер телефона, місто')'''

	def __init__(self, contact_quantity):
		'''Ініціалізуємо змінні'''
		self.source_file = "Phone_book.json" # Файл для результатів
		self.data = open(self.source_file, mode = 'w') 

		self.new = {} # Словник для пошуку в файлі
		self.data_dict = {} # Словник для запису в файл
		self.secondary_dict = {} # Словник для запису в файл
		self.contact_quantity = contact_quantity # Кількість записів щоб записати в файл 


	def Add_new_contact(self):
		'''Доавляємо новий контакт''' 

		for i in range(1, self.contact_quantity + 1):
			print('\tPerson № {}'.format(i))
			
			# Створюємо словник за характеристиками (ім'я, фамілія, номер телефона, місто)
			self.secondary_dict['name'] = input('First name: ')
			self.secondary_dict['second name'] = input('Second name: ')
			self.secondary_dict['full name'] = self.secondary_dict['name'] + ' ' + self.secondary_dict['second name']
			self.secondary_dict['phone'] = input('Phone number: ')
			self.secondary_dict['city'] = input('City: ')

			# Добавляємо створений словник в новий з ключами (1, 2, 3, і т.д.)
			self.data_dict[i] = self.secondary_dict.copy()

			print()	
		
		json.dump(self.data_dict, self.data) # Записуємо результати в файл
		self.data.close()


	def Find_in_book(self):
		'''Пошук по файлові (не можливий якщо записи в файл не додані)'''

		self.data = open(self.source_file, mode = 'r')
		self.new = json.load(self.data) # Витягуємо данні з файла

		# Вводимо параметр, по якому здійснювати пошук
		search = input('Type the person attribute (Name or phone or city): ')

		# Реалізація пошуку
		for q in self.new.values():
			if search in q.values():
				print('-' * 30)
				for i, j in q.items():
					print('\t', i, '-', j)
				print('-' * 50)
			else:
				print('There is no record with attribute: "{}"'.format(search))

		self.data.close()


	def Delete_form_book(self):
		'''Видаляємо запис з певним атрибутом з файла (не можливий якщо записи в файл не додані)'''

		self.data = open(self.source_file, mode = 'r')
		self.new = json.load(self.data) # Витягуємо данні з файла

		# Вводимо параметр, по якому здійснювати пошук
		search = input('Type the person attribute which you want to delete from book: ')
		self.data.close()
		
		# Реалізація пошуку
		for k, v in self.new.items():
			if search in v.values():
				tmp = k
				print('Person with attribute: "{}"'.format(search) + ' has been removed from book')

		# Видалення об'єкта з словника
		self.new.pop(tmp)

		# Переписуємо відкореговані данні в файл
		self.data = open(self.source_file, mode = 'w')
		json.dump(self.new, self.data)
		self.data.close()
