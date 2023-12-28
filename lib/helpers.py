import os
import sys
from models.display import Display
from models.cube import *

title_screen = Display(
    title = "RubixCube Simulator",
    content = "Personal project by Elijah Kollie 2023",
    options = [
        "1. Play",
        "2. Help",
        "3. Quit"
    ]
)

cube_screen = Display(
    title = "Rubix cube", 
    content = cube.print_cube(),
    options = [
        "1. Rotate Face",
        "2. View Face",
        "3. Return"
    ], 
    width=38,
)



face_screen = Display(
    title= "Select a Face Below", 
    content= cube_screen.content,
    options=[
        "1. Front",
        "2. Left",
        "3. Right",
        "4. Top",
        "5. Bottom",
        "6. Back",
        "7. Return",
    ], 
    width=38,
)

direction_prompt = Display(
    title = cube_screen.title,
    content = cube_screen.content,
    options=[
        "1. Clockwise",
        "2. Counter-clockwise"
    ],
    width = 38,
)


help_screen = Display(
    title="Help Page", 
    content="Place holder",
    options=[
        "1. Return",
    ],
    width=38, 
)

def title_menu(recurred = False):
    # Clear the console screen
    os.system("clear")
    # Extract lowercase options for easier comparison
    options = [option.lower() for option in title_screen.options]
    # Display the title screen
    title_screen.print_screen()
    # Shows error if user inputs invalid command
    if recurred: print("Please input valid command")
    # Get user input
    selection = input("> ")
    # Checks user input
    if selection.lower() in options[0]:
        start_game()
    elif selection.lower() in options[1]:
        help_menu()
    elif selection.lower() in options[2]:
        sys.exit()
    # Keeps prompting for valid input until one is received
    title_menu(recurred = True)


def start_game(recurred = False):
    os.system("clear")
    options = [option.lower() for option in cube_screen.options]
    cube_screen.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:
        face_select(mode = "Face")
    elif selection.lower() in options[1]:
        face_select(mode = "Cube")
    elif selection.lower() in options[2]:
        title_menu()
    start_game(recurred = True)

def help_menu(recurred = False):
    os.system("clear")
    options = [option.lower() for option in help_screen.options]
    help_screen.print_screen()  
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:
        title_menu()
    help_menu(recurred = True)


def face_select(mode, recurred = False):
    os.system("clear")
    options = [option.lower() for option in face_screen.options]
    face_screen.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:
        if mode == "Face":
            rotate_front()
        elif mode == "Cube":
            cube.current_view_face = "Front"
            update_face()
    elif selection.lower() in options[1]:
        if mode == "Face":
            rotate_left()
        elif mode == "Cube":
            cube.current_view_face = "Left"
            update_face()
    elif selection.lower() in options[2]:
        if mode == "Face":
            rotate_right()
        elif mode == "Cube":
            cube.current_view_face = "Right"
            update_face()
    elif selection.lower() in options[3]:
        if mode == "Face":
            rotate_top()
        elif mode == "Cube":
            cube.current_view_face = "Top"
            update_face()
    elif selection.lower() in options[4]:
        if mode == "Face":
            rotate_bottom()
        elif mode == "Cube":
            cube.current_view_face = "Bottom"
            update_face()
    elif selection.lower() in options[5]:
        if mode == "Face":
            rotate_back()
        elif mode == "Cube":
            cube.current_view_face = "Back"
            update_face()
    elif selection.lower() in options[6]:
        start_game()
    face_select(recurred = True, mode=mode)





###### Cube interaction ######
def rotate_front(recurred = False):
    os.system("clear")
    options = [option.lower() for option in direction_prompt.options]
    direction_prompt.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:   
        cube.rotate_front_clockwise()

    elif selection.lower() in options[1]: 
        cube.rotate_front_counter_clockwise()
    update_face()
    rotate_front(recurred = True)

def rotate_left(recurred = False):
    os.system("clear")
    options = [option.lower() for option in direction_prompt.options]
    direction_prompt.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:   
        cube.rotate_left_clockwise()

    elif selection.lower() in options[1]: 
        cube.rotate_left_counter_clockwise()
    update_face()
    rotate_left(recurred = True)

def rotate_right(recurred = False):
    os.system("clear")
    options = [option.lower() for option in direction_prompt.options]
    direction_prompt.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:   
        cube.rotate_right_clockwise()

    elif selection.lower() in options[1]: 
        cube.rotate_right_counter_clockwise()
    update_face()
    rotate_right(recurred = True)

def rotate_top(recurred = False):
    os.system("clear")
    options = [option.lower() for option in direction_prompt.options]
    direction_prompt.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:   
        cube.rotate_top_clockwise()

    elif selection.lower() in options[1]: 
        cube.rotate_top_counter_clockwise()
    update_face()
    rotate_top(recurred = True)

def rotate_bottom(recurred = False):
    os.system("clear")
    options = [option.lower() for option in direction_prompt.options]
    direction_prompt.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:   
        cube.rotate_bottom_clockwise()

    elif selection.lower() in options[1]: 
        cube.rotate_bottom_counter_clockwise()
    update_face()
    rotate_bottom(recurred = True)

def rotate_back(recurred = False):
    os.system("clear")
    options = [option.lower() for option in direction_prompt.options]
    direction_prompt.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:   
        cube.rotate_back_clockwise()

    elif selection.lower() in options[1]: 
        cube.rotate_back_counter_clockwise()
    update_face()
    rotate_back(recurred = False)

def update_face():
    cube_screen.content = cube.print_cube()
    face_screen.content = cube.print_cube()
    direction_prompt.content = cube.print_cube()
    start_game()

