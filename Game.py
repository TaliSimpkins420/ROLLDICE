import random
import time

def roll_dice():
    print("\n🎲 Rolling the dice...")
    time.sleep(1)  # delay for dramatic effect
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"You rolled a {die1} and a {die2}!")
    print(f"Total: {die1 + die2}\n")

def main():
    print("""
    🎲 Welcome to the Dice Rolling Simulator! 🎲
    Type 'roll' to roll the dice or 'quit' to exit.
    """)

    while True:
        user_input = input("What would you like to do? (roll/quit): ").strip().lower()

        if user_input == 'roll':
            roll_dice()
        elif user_input == 'quit':
            print("Thanks for playing! Goodbye 👋\n")
            break
        else:
            print("Invalid input. Please type 'roll' or 'quit'.\n")

if __name__ == '__main__':
    main()
