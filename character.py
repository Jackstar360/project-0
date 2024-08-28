class Character:
    """
    Represents a character in the game.
    
    Attributes:
        name (str): The name of the character.
        health (int): The current health of the character.
        inventory (list): The items in the character's inventory.
        dialogue (dict): The dialogue responses for the character.
    
    Methods:
        talk_to_player(player_msg: str) -> None:
            Prints the character's dialogue response for the given player message.
        receive_item(item: Any) -> None:
            Adds the given item to the character's inventory.
    """
    def __init__(self, name, health, inventory, dialoge):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.dialoge = dialogue

    def talk_to_player(self, player_msg):
        for sentance in self.dialogue:
            if player_msg == sentance:
                print(self.dialoge(sentance))

    def receive_item(self, item):
        self.inventory.append(item)