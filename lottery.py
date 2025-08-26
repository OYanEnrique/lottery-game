# Lottery
from time import sleep
from random import randint

game_list = []
user_list = []

print('------Lottery Game------')

while len(user_list)<6:
	user_game = int(input('Enter your game: [6 numbers, one at a time]\n'))
	if user_game not in user_list:
		user_list.append(user_game)
user_list.sort()
print(f'Your Game: {user_list}\n')
	
games = int(input('How many games do you want me to draw?\n'))

while True:
	for c in range (0, games):
		temp_game = []
		while len(temp_game) <6:
			number = randint(1, 60)
			if number not in temp_game:
				temp_game.append(number)
	
		temp_game.sort()
		game_list.append(temp_game[:])
		temp_game.clear()
		
	print(f'\n------Drawing {games} lottery tickets------\n')
	for i, game in enumerate(game_list):
		print(f'Game {i+1}: {game}') 
		sleep(1)
		
	if user_list in game_list:
		print('\nCongratulations! YOU WON!')
	else:
		print('\nBetter luck next time. Try again!')
		
	try_again = str(input(f'\nDraw more {games} games? [y/n]')).strip().lower()[0]
	if try_again == 'n':
		print('\nSee you soon!\n')
		break