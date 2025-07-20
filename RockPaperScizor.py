from random import choice

game_choice=['rock', 'paper', 'scizor']
cpu_choice=choice(game_choice)
player_choice=input('Choose between Rock, Paper or Scizor:').lower()

print(f'The Cpu chose {cpu_choice}!\n')
print(f'You chose {player_choice}!\n')

if player_choice == 'rock' and cpu_choice == 'scizor' or player_choice == 'scizor' and cpu_choice == 'paper' or player_choice == 'paper' and cpu_choice == 'rock':
	print("You Won!")
elif player_choice == cpu_choice:
	print("Draw!")
else:
	print("You lost!")
