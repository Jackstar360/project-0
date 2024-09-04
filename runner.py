import sys
import readchar
from character import Character
from item import Item
from wordle import playWordle

menuPlace = 1

def deleteLines(num_lines=1):
    for _ in range(num_lines):
        sys.stdout.write('\033[F')  # Move cursor up one line
        sys.stdout.write('\033[K')  # Clear the line
    sys.stdout.flush()  # Ensure the output is displayed immediately
# deletes the last line(s), made by cody

def handle_key_press():
    global menuPlace
    key = readchar.readkey()
    
    if key == readchar.key.RIGHT:
        print("Right key clicked")
    elif key == readchar.key.LEFT:
        print("Left key clicked")
    elif key == readchar.key.UP:
        print("Up key clicked")
        if menuPlace > 1:
            menuPlace -= 1
        else:
            menuPlace = 4
        deleteLines(5)
    elif key == readchar.key.DOWN:
        print("Down key clicked")
        if menuPlace < 4:
            menuPlace += 1
        else:
            menuPlace = 1
        deleteLines(5)
    elif key == readchar.key.ESC:
        exit()
    elif key == readchar.key.ENTER:
        print("Enter key clicked")
        handle_menu_selection()
    
    storeMenu()

def handle_menu_selection():
    if menuPlace == 1:
        print("You picked the Hot Dog Cart!")
    elif menuPlace == 2:
        print("You picked the Hot Dog Stand!")
    elif menuPlace == 3:
        print("You picked the Hot Dog Truck!")
    elif menuPlace == 4:
        print("You picked the Hot Dog Store Front!")

def storeMenu():
    menu_options = [
        "[10]Hot Dog Cart",
        "[250]Hot Dog Stand",
        "[650]Hot Dog Truck",
        "[1500]Hot Dog Store Front"
    ]
    
    for i, option in enumerate(menu_options, 1):
        if i == menuPlace:
            print(f"{option} ⬅")
        else:
            print(option)

print("""Welcome to Hot Dog Simulator!
Pick your Hot Dog Selling Location""")

storeMenu()

while True:
    handle_key_press()

# The rest of your code remains the same
d1 = input("You come up to a field and see a star! do you want to pick it up? (y/n)")
if d1 == "y":
    star = Item("Star", "A Shiny Star", 10)
    print("You picked up the star! now you see a dude. want to talk to him? (y/n)")
    d1a = input()
    if d1a == "y":
        character = Character("Dude", 10, [], {"Hello": "Hi! I'm a dude"})