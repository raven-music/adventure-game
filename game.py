import random
import time
import os
import sys
import msvcrt

animal = ["frog", "bug", "toad", "and chill rat", "wurm", "human male"]

def intro_animation(delay):
    with open("images/intro/intro1.txt", 'r') as file:
        file_contents = file.read()
        print(file_contents)
    time.sleep(delay)
    with open("images/intro/intro2.txt", 'r') as file:
        file_contents = file.read()
        print(file_contents)
    time.sleep(delay)
    with open("images/intro/intro3.txt", 'r') as file:
        file_contents = file.read()
        print(file_contents)
    time.sleep(delay)
    with open("images/intro/intro4.txt", 'r') as file:
        file_contents = file.read()
        print(file_contents)
    time.sleep(delay)
    with open("images/intro/intro5.txt", 'r') as file:
        file_contents = file.read()
        print(file_contents)
    time.sleep(delay)
    with open("images/intro/intro6.txt", 'r') as file:
        file_contents = file.read()
        print(file_contents)
    time.sleep(3)


def show_image(path):
    with open(path, 'r') as file:
        file_contents = file.read()
        print(file_contents)

typingInProgress = True

def show_text_slowly(text, delay=0.05, delay_after_period=0.8):
    for char in text:
        if msvcrt.kbhit() and msvcrt.getch() == b' ':  # Check if the spacebar is NOT pressed
            delay = 0

        print(char, end='', flush=True) 
        if char == '.':
            time.sleep(delay_after_period)
        elif char == ',':
            time.sleep(0.4)
        else:
            time.sleep(delay)
    print()         

def show_ascii_art(path, delay=0.1):
    with open(path, 'r') as file:
        for line in file:
            print(line.rstrip())
            time.sleep(delay)    

scenarios = {
    'start': {
        'description': "You are waking up in a dark forest. You do not remember how you got here. "
                       "What will you do?",
        'choices': {
            'hang around': 'hanging',
            'leave': 'leaving'
        }
    },
    'hanging': {
        'description': "You hung around for a while. You found a cool " + random.choice(animal) + ". "
                       "Do you want to hang out some more or leave?",
        'choices': {
            'hang': 'hanging',
            'leave': 'leave_animal'
        }
    },
    'leaving': {
        'description': "You start walking in a random direction. Eventually you find a large river of water. "
                       "Follow the stream upwards or downwards?",
        'choices': {
            'upwards': 'upwards_stream',
            'downwards': 'downwards_stream',
            'try to jump it': 'jump_river'
        }
    },
    'leave_animal': {
        'description': "You gave the little fella a pet and left. You walk in a random direction filled with joy, because of your new friend. "
                       "Your friend gave you inspiration. You found a cool tree. Climb it or continue walking?",
        'choices': {
            'climb': 'climb_tree',
            'continue': 'continue_path'
        }
    },
    'upwards_stream': {
        'description': "You walk by the riverbed against the stream. You hope to find a higher vantage point to see where you are. You keep walking, but it does not seem like you are getting any higher. "
                       "What will you do?",
        'choices': {
            'Keep walking upwards': 'keep_walking_upwards',
            'Go down': 'downwards_stream'
        }
    },
    'downwards_stream': {
        'description': "You walk by the riverbed following the stream. "
                       "Congratulations, you dead!",
        'choices': {}
    },
    'jump_river': {
        'description': "You are feeling yourself. You take a few steps back.  "
                       "You try to jump the river. Not surprisingly, you fall in. What will you do?",
        'choices': {
            'Swim to shore': 'die_instantly',
            'Let the stream take you': 'swim_stream'
        }
    },
    'swim_stream':{
        'description': "You let the stream take you... The current is powerfull, but you manage to keep your head above the dark water. In the distance you see a tree branch hanging above the water. "
                        "What will you do?",
        'choices': {
            'Grab branch': "grab_branch",
            'Keep swimming': "keep_swimming"
        }
    },
    'climb_tree': {
        'description': "You climb the tree. The tree consumes you. You are the tree now. ",
        'choices': {}
    }, 
    'continue_path': {
        'description': "You continue on the path and get lost in the woods. "
                       "Game over!",
        'choices': {}
    },
    'die_instantly': {
        'description': "You chose death. death you will receive. ",
        'choices': {}
    }
}

def play_game():
    show_ascii_art("images/tree.txt")
    current_scenario = 'start'

    while True:
        scenario = scenarios[current_scenario]
        show_text_slowly(scenario['description'])  # Show text slowly.

        # Check if there are choices to make.
        if not scenario['choices']:
            break

        # Display available choices with numbers.
        print("\nChoices:")
        for i, (choice, next_scenario) in enumerate(scenario['choices'].items(), start=1):
            show_text_slowly(f"{i}. {choice.capitalize()}", delay=0.02)  # Show choices slowly.

        # Get the player's choice as a number.
        while True:
            try:
                choice_number = int(input("Enter the number of your choice: "))
                if 1 <= choice_number <= len(scenario['choices']):
                    break
                else:
                    print("Invalid choice number. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        # Map the number to the corresponding choice.
        player_choice = list(scenario['choices'].keys())[choice_number - 1]

        print()
        # Update the current scenario based on the player's choice.
        current_scenario = scenario['choices'][player_choice]

        # Check if there is ASCII art to display for the current scenario.
        ascii_art_file = f"ascii_art/{current_scenario}.txt"
        if os.path.isfile(ascii_art_file):
            show_ascii_art(ascii_art_file)

# Start the game.
if __name__ == "__main__":
    intro_animation(0.6)
    play_game()
