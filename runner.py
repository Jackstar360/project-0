import sys
import readchar
import time
import random
from character import Character
from item import Item

cash = 2000
menuPlace = 1
selectingShop = True
playLoop = False

events = {
    "Guy with glasses": 1,
    "Lady with hat": 1,
    "Hungry businessman": 2,
    "College student": 1,
    "Food critic": 3,
    "Tourist family": 2,
    "Picky eater": 2,
    "Vegetarian customer": 2,
    "Food blogger": 3,
    "Late-night partier": 1,
    "Health inspector": 4,
    "Celebrity in disguise": 3,
    "Competitive eater": 2,
    "Elderly couple": 1,
    "Group of teenagers": 2
}
#got help from cody to generate the events
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
        deleteLines(6)
    elif key == readchar.key.DOWN:
        print("Down key clicked")
        if menuPlace < 4:
            menuPlace += 1
        else:
            menuPlace = 1
        deleteLines(6)
    elif key == readchar.key.ESC:
        exit()
    elif key == readchar.key.ENTER:
        print("Enter key clicked")
        selectingShop = True
        handle_menu_selection()
    storeMenu()

def handle_menu_selection():
    global selectingShop
    global cash
    if menuPlace == 1 and cash >= 10:
        cash -= 10
        selectingShop = False
        deleteLines(6)
        print("You picked the Hot Dog Cart!")
    elif menuPlace == 1 and cash < 10:
        selectingShop = True
        deleteLines(6)
        print("You don't have enough money!")
        time.sleep(1)
        deleteLines(1)
    elif menuPlace == 2 and cash >= 250:
        cash -= 250
        selectingShop = False
        deleteLines(6)
        print("You picked the Hot Dog Stand!")
    elif menuPlace == 2 and cash < 250:
        selectingShop = True
        deleteLines(6)
        print("You don't have enough money!")
        time.sleep(1)
        deleteLines(1)
    elif menuPlace == 3 and cash >= 650:
        cash -= 650
        selectingShop = False
        deleteLines(6)
        print("You picked the Hot Dog Truck!")
    elif menuPlace == 3 and cash < 650:
        selectingShop = True
        deleteLines(6)
        print("You don't have enough money!")
        time.sleep(1)
        deleteLines(1)
    elif menuPlace == 4 and cash >= 1500:
        cash -= 1500
        selectingShop = False
        deleteLines(6)
        print("You picked the Hot Dog Store Front!")
    elif menuPlace == 4 and cash < 1500:
        selectingShop = True
        deleteLines(6)
        print("You don't have enough money!")
        time.sleep(1)
        deleteLines(1)

def storeMenu():
    global menu_options
    if selectingShop == True:
        print("Cash: " + str(cash))
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

while selectingShop == True:
    handle_key_press()



def eventHandler(event):
    global playLoop
    while playLoop == True:
        event = random.choice(list(events.keys()))
        eventHandler(event)
