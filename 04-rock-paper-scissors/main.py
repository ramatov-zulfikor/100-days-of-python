import random

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

rpc_list = [rock, paper, scissors]

user_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))
bot_answer = random.randint(0, 2)

if user_answer > 2 or user_answer < 0:
	print("You typed an invalid number. You lose!")
else:
	print(rpc_list[user_answer])
	print("Computer chose:")
	print(rpc_list[bot_answer])
	if user_answer == 0 and bot_answer == 2:
		print("You win!")
	elif bot_answer == 0 and user_answer == 2:
		print("You lose!")
	elif user_answer > bot_answer:
		print("You win!")
	elif bot_answer > user_answer:
		print("You lose!")
	elif user_answer == bot_answer:
		print("It's draw!")
	else:
		print("Somethind went wrong. Try again.")
