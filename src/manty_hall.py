import random
from typing import Tuple

def monty_hell_game(switch_doors: bool) -> bool:
    """Simulates one round of the Monty Hall game.

    In this simulation, there are three doors: one hides an "Expensive Car" and the other two hide goats.
    The doors are randomly shuffled, and the contestant makes an initial random choice.
    If `switch_doors` is True, the host reveals one of the remaining doors that contains a goat,
    and the contestant switches to the only other unopened door.
    If `switch_doors` is False, the contestant sticks with the initial choice.
    The function returns True if the final choice leads to the "Expensive Car", otherwise it returns False.

    :param switch_doors: Determines whether the contestant switches their choice after a goat door is revealed.
                         True to switch, False to stick with the initial choice.
    :type switch_doors: bool
    :return: True if the final chosen door contains the "Expensive Car", False otherwise.

    """
    doors = ["goat", "goat", "Expensive Car"]
    
    random.shuffle(doors)
    
    initial_choice = random.choice(range(3)) 
    if switch_doors:
        door_revealeds = [i for i in range (3) if doors[i] != "Expensive Car" and i != initial_choice]
        del doors[initial_choice]
        doors.insert(initial_choice, None)
        door_revealed = random.choice(door_revealeds)
        
        del doors[door_revealed]    
        doors.remove(None)
        final_choice = doors[0]
    else:
        final_choice = doors[initial_choice]
        
    return final_choice == "Expensive Car"

def simulate_game(number_counter: int) -> tuple[int, int]:
    """This function examines the percentage of switching choice in the user and the percentage of sticking with the initial choice.

    :param number_counter: The number of times this operation is performed.
    :return: The number of times the user won by switching and the number of times the user won without switching.
    """
    num_words_without_switching = sum([monty_hell_game(False) for _ in range(number_counter)])
    num_words_with_switching = sum([monty_hell_game(True) for _ in range(number_counter)])
    return num_words_with_switching, num_words_without_switching


if __name__ == "__main__":
    number_count = 100000
    print(simulate_game(number_count))