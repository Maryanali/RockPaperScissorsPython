#!/usr/bin/env python3
import random
#added ascii of rock paper scissors

rock = '''
		_______
---'   ____)
			(_____)
			(_____)
			(____)
---.__(___)
'''

paper = '''
		_______
---'   ____)____
					______)
					_______)
					_______)
---.__________)
'''

scissors = '''
		_______
---'   ____)____
					______)
				__________)
			(____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
computer_choice = random.randint(0,2)
if user_choice >= 3 or user_choice < 0:
	print("You typed an invalid number")
else: 
	
	print(f"You chose {user_choice}")
	print(game_images[user_choice])
	print(f"Computer chose {computer_choice}")
	print(game_images[computer_choice])
	
	
	
	#computer_choice = ["rock", "paper", "scissors"]
	#print(random.choice(computer_choice) )
	
	
	if user_choice == 0 and computer_choice == 2:
		print("You win!")
	elif computer_choice > user_choice:
		print("You lose")
	elif computer_choice == user_choice:
		print("Its a draw")
	elif user_choice == 2 and computer_choice == 0:
		print("You lose")
	elif user_choice > computer_choice:
		print("You win")
	elif user_choice >= 3 or user_choice < 0:
		print("You typed an invalid number")

	