# character.py

class Character:
    def __init__(self, name, char_class, strength, agility, intelligence):
        self.name = name
        self.char_class = char_class
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.hp = 100
        self.max_hp = 100
        self.inventory = []
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

    def display_stats(self):
        print("\n=== Character Stats ===")
        print(f"Name: {self.name}")
        print(f"Class: {self.char_class}")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}/{self.xp_to_next_level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Inventory: {self.inventory}")
        print("========================\n")

    def view_inventory(self):
        print("\nInventory:")
        if self.inventory:
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("You have nothing in your inventory.")

    def gain_xp(self, amount):
        print(f"\nYou gained {amount} XP!")
        self.xp += amount

        while self.xp >= self.xp_to_next_level:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)

        self.strength += 1
        self.agility += 1
        self.intelligence += 1
        self.max_hp += 10
        self.hp = self.max_hp

        print(f"\nLEVEL UP! You are now level {self.level}.")
        print("You feel stronger!")
        self.display_stats()

    def use_item(self, item_name):
        item_name_lower = item_name.lower()

        for item in self.inventory:
            if item.lower() == item_name_lower:
                if item == "Healing Potion":
                    if self.hp == self.max_hp:
                        print("You are already at full health.")
                        return
                    heal_amount = 25
                    self.hp = min(self.hp + heal_amount, self.max_hp)
                    self.inventory.remove(item)
                    print(f"\nYou drink the Healing Potion and restore {heal_amount} HP! Current HP: {self.hp}/{self.max_hp}")
                    return
                else:
                    print(f"You can't use {item}.")
                    return
            
        print(f"You don't have {item_name} in your inventory.")
