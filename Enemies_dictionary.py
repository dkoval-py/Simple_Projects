# Libary for random function
import random

# Dictionary with enemy's characteristics
first_enemy = {
	'position_x' : 52,
	'position_y' : 20,
	'health': 100,
	'health_color' : ['Green', 'Orange', 'Red'],
	'name' : '',
	'face_image': ['face1.jpg', 'face2.jpg', 'face3.jpg'],
}

# Names' array
enemy_names = ['John', 'Cobby', 'Joordan', 'Cody', 'Johan', 'Jim', 'Bernard', 'Alex', 'Villiam', 'Rendy']
# Enemies' array
enemy_list = []

# Creating 10 enemies and setting different characteristics for them
for i in range(0, 10):
	first_enemy['name'] = enemy_names[i]
	first_enemy['health'] = int(random.uniform(0, 100))
	first_enemy['position_x'] = int(random.uniform(-50, 50))
	first_enemy['position_y'] = int(random.uniform(0, 100))
	enemy_list.append(first_enemy.copy())

# Print our enemies
for enem in enemy_list:
	# Setting the different names' color and face image
	if enem['health'] == 100:
		enem['health_color'] = enem['health_color'][0]
		enem['face_image'] = enem['face_image'][0]
	elif enem['health'] < 100 and enem['health'] >= 40:
		enem['health_color'] = enem['health_color'][1]
		enem['face_image'] = enem['face_image'][1]
	elif enem['health'] < 39:
		enem['health_color'] = enem['health_color'][2]
		enem['face_image'] = enem['face_image'][2]
	
	print(enem)
