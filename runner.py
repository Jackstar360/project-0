import sys
from pynput import keyboard
from pynput.keyboard import Key
from character import Character
from item import Item
from wordle import playWordle

def deleteLines(num_lines=1):
    for _ in range(num_lines):
        sys.stdout.write('\033[F')  # Move cursor up one line
        sys.stdout.write('\033[K')  # Clear the line
    sys.stdout.flush()  # Ensure the output is displayed immediately
# deletes the last line(s), made by cody

def on_key_release(key):
    if key == Key.right:
        print("Right key clicked")
    elif key == Key.left:
        print("Left key clicked")
    elif key == Key.up:
        print("Up key clicked")
    elif key == Key.down:
        print("Down key clicked")
    elif key == Key.esc:
        exit()
    elif key == Key.enter:
        print("Enter key clicked")

print("Welcome to Hot Dog Simulator!")
print("Pick your Hot Dog Selling Location")
print("""Hot Dog Cart ⬅
Hot Dog Stand
Hot Dog Truck
Hot Dog Store Front""")
if key == Key.enter:
  print("You picked the Hot Dog Cart!")
elif key == Key.down:
  


d1 = input("You come up to a field and see a star! do you want to pick it up? (y/n)")
if d1 == "y":
  star = Item("Star", "A Shiny Star", 10)
  print("You picked up the star! now you see a dude. want to talk to him? (y/n)")
  if d1a == "y":
    character = Character("Dude", 10, [], {"Hello": "Hi! I'm a dude"})

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()