import random

# Define the game's scenarios as dictionaries.
# Each scenario has a description and possible choices.
animal = ["frog", "bug", "toad", "and chill rat", "wurm", "human male"]

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
        'description': "You walk by the riverbed against the stream. "
                       "Congratulations, you dead!",
        'choices': {}
    },
    'downwards_stream': {
        'description': "You walk by the riverbed following the stream. "
                       "Congratulations, you dead!",
        'choices': {}
    },
    'jump_river': {
        'description': "You are feeling yourself. You take a few steps back.  "
                       "You try to jump the river. Surprisingly you make it.",
        'choices': {
            'die?': 'die_instantly'
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

# Define a function to play the game.
def play_game():
    current_scenario = 'start'

    while True:
        scenario = scenarios[current_scenario]
        print(scenario['description'])

        # Check if there are choices to make.
        if not scenario['choices']:
            break

        # Display available choices.
        print("Choices:")
        for choice, next_scenario in scenario['choices'].items():
            print(f"- {choice.capitalize()}")

        # Get the player's choice.
        player_choice = input("What do you choose? ").lower()

        # Check if the choice is valid.
        if player_choice in scenario['choices']:
            current_scenario = scenario['choices'][player_choice]
        else:
            print("Invalid choice. Try again.")

# Start the game.
if __name__ == "__main__":
    play_game()
