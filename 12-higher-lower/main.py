from art import logo, vs
from replit import clear
from random import choice
from game_data import data

def format_data(comparison):
    name = comparison["name"]
    descr = comparison["description"]
    country = comparison["country"]
    return f"{name}. {descr} from {country}."

def check_answer(answer, a, b):
    if a > b:
        return answer == "a"
    else:
        return answer == "b"

print(logo)
score = 0
should_continue = True
comparison_b = choice(data)

while should_continue:
    comparison_a = comparison_b
    comparison_b = choice(data)
    if comparison_a == comparison_b:
        comparison_b = choice(data)

    print(f"Compare A: {format_data(comparison_a)}")
    print(vs)
    print(f"Against B: {format_data(comparison_b)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = comparison_a["follower_count"]
    b_follower_count = comparison_b["follower_count"]
    is_correct = check_answer(answer, a_follower_count, b_follower_count)

    clear()

    if is_correct:
        score += 1
        print(f"You're right! Your current score {score}")
    else:
        should_continue = False
        print(f"That's wrong. Your final score {score}")
