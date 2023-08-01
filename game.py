import time

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_choice(choices):
    while True:
        choice = input("> ").strip().lower()
        if choice in choices:
            return choice
        print("Invalid choice. Try again.")

def game_intro():
    delay_print("Welcome to the Python Adventure Game!")
    delay_print("You find yourself standing in front of a mysterious cave.")
    delay_print("Do you want to enter the cave or explore the surroundings?")
    return get_choice(["enter", "explore"])

def explore_surroundings():
    delay_print("You decide to explore the surroundings.")
    delay_print("You find a hidden treasure chest!")
    delay_print("Do you want to open it or leave it?")
    return get_choice(["open", "leave"])

def open_treasure_chest():
    delay_print("You open the treasure chest and find a shiny gem!")
    delay_print("Congratulations, you won the game!")

def enter_cave():
    delay_print("You cautiously enter the dark cave.")
    delay_print("Inside the cave, you encounter a dragon!")
    delay_print("Do you want to fight the dragon or run away?")
    return get_choice(["fight", "run"])

def fight_dragon():
    delay_print("You decide to fight the dragon.")
    delay_print("You bravely face the dragon, but it's too powerful.")
    delay_print("The dragon defeats you. Game over.")

def run_away():
    delay_print("You turn around and run as fast as you can.")
    delay_print("Luckily, you manage to escape from the cave.")
    delay_print("You made it out alive!")

def play_game():
    choice = game_intro()

    if choice == "explore":
        choice = explore_surroundings()
        if choice == "open":
            open_treasure_chest()
        elif choice == "leave":
            delay_print("You decide to leave the treasure chest behind.")
            delay_print("You continue your adventure.")
    elif choice == "enter":
        choice = enter_cave()
        if choice == "fight":
            fight_dragon()
        elif choice == "run":
            run_away()

if __name__ == "__main__":
    play_game()
