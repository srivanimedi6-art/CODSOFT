# rock_paper_scissors.py
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid! Please enter rock, paper, or scissors: ").lower()
    return choice

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("\n--- ROCK PAPER SCISSORS GAME ---")
    user_score = 0
    comp_score = 0

    while True:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()

        print(f"\n🧍‍♂️ You chose: {user_choice}")
        print(f"💻 Computer chose: {comp_choice}")

        result = decide_winner(user_choice, comp_choice)
        print(f"🎯 {result}")

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            comp_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {comp_score}")

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    main()