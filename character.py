# character.py

class Character:
    def __init__(self, name, char_class, strength, agility, intelligence):
        self.name = name
        self.char_class = char_class
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.hp = 100
        self.inventory = []

    def display_stats(self):
        print("\n=== Character Stats ===")
        print(f"Name: {self.name}")
        print(f"Class: {self.char_class}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")
        print(f"HP: {self.hp}")
        print(f"Inventory: {self.inventory}")
        print("========================\n")