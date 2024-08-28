from character import Character
from item import Item
from wordle import playWordle

print("Welcome to the game!")
d1 = input("You come up to a field and see a star! do you want to pick it up? (y/n)")
if d1 == "y":
  star = Item("Star", "A Shiny Star", 10)
  print("You picked up the star! now you see a dude. want to talk to him? (y/n)")
  if d1a == "y":
    character = Character("Dude", 10, [], {"Hello": "Hi! I'm a dude"})