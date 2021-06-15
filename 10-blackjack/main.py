from replit import clear
from random import choice
from art import logo

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play_game == "y":
    play_game = True
else:
    play_game = False

def has_blackjack(user_cards, computer_cards):
    if sum(user_cards) == 21 and sum(computer_cards) == 21:
        return "It's draw!"
    elif sum(user_cards) == 21:
        return "Hey, you achieved 21. You win!"
    elif sum(computer_cards) == 21:
        return "Computer achieved 21. You lose!"
    else:
        return False

def over_blackjack(cards):
    if sum(cards) > 21:
        return True
    else:
        return False

def show_hands():
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, his final score {sum(computer_cards)}")


while play_game:
    print(logo)

    for _ in range(2):
        user_cards.append(choice(cards))
        computer_cards.append(choice(cards))
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    if has_blackjack(user_cards, computer_cards) != False:
        print(has_blackjack(user_cards, computer_cards))
        break
    
    if over_blackjack(user_cards):
        print("You went over. You lose!")
        break

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == "y":
        another_card = True
    else:
        another_card = False

    while another_card:
        user_cards.append(choice(cards))
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        if has_blackjack(user_cards, computer_cards) != False:
            print(has_blackjack(user_cards, computer_cards))
            break

        if over_blackjack(user_cards):
            print("You went over. You lose!")
            break

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if another_card == "y":
            another_card = True
        else:
            another_card = False

    if sum(user_cards) < 21:
        if sum(computer_cards) < 17:
            computer_cards.append(choice(cards))

        show_hands()
        if over_blackjack(computer_cards):
            print("Computer went over. You win!")
        else:
            if sum(user_cards) == 21 and sum(computer_cards) == 21:
                print("It's draw!")
            elif sum(user_cards) == 21:
                print("Hey, you achieved 21. You win!")
            elif sum(computer_cards) == 21:
                print("Computer achieved 21. You lose!")
            elif sum(user_cards) > sum(computer_cards):
                print("Hey, your total score is higher than computer. You win!")
            elif sum(user_cards) < sum(computer_cards):
                print("Computer's total score higher. You lose!")
            else:
                print("WTF?")

    play_game = input("Do you want to play again a game of Blackjack? Type 'y' or 'n': ")

    if play_game == "y":
        play_game = True
        user_cards = []
        computer_cards = []
        clear()
    else:
        play_game = False
