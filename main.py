# main.py

from character import Character
from scenes.intro import intro_scene
from world import world_map
from combat import start_combat

def create_character():
    print("Welcome to the Lands of Eldoria!")
    name = input("What is your character's name? ")

    print("\nChoose your class:")
    print("1. Warrior (strong and tough)")
    print("2. Rogue (fast and stealthy)")
    print("3. Mage (powerful magic user)")

    while True:
        class_choice = input("Enter class number (1-3): ")
        if class_choice == "1":
            char_class = "Warrior"
            break
        elif class_choice == "2":
            char_class = "Rogue"
            break
        elif class_choice == "3":
            char_class = "Mage"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("\nYou have 10 stat points to distribute between Strength, Agility, and Intelligence.")

    points = 10
    strength = agility = intelligence = 0

    while points > 0:
        print(f"\nPoints remaining: {points}")
        try:
            s = int(input("Add to Strength: "))
            a = int(input("Add to Agility: "))
            i = int(input("Add to Intelligence: "))

            if s + a + i != points:
                print("Total points must equal your remaining points. Try again.")
                continue

            strength, agility, intelligence = s, a, i
            break
        except ValueError:
            print("Please enter valid numbers.")

    player = Character(name, char_class, strength, agility, intelligence)
    return player

def explore_world(player):
    current_location = "Dunwich"

    while True:
        room = world_map[current_location]
        print(f"\nLocation: {current_location}")
        print(room["description"])

        if "enemy" in room:
            enemy = room["enemy"]
            survived = start_combat(player, enemy)
            if survived:
                del room["enemy"]
            else:
                print("You failed to escape the battle.")
                return

        print("\nAvailable directions:")
        for direction in room["exits"]:
            print(f" - {direction.title()}")

        command = input("\nWhat do you want to do? (go [direction] / look / inventory / quit): ").lower()

        if command.startswith("go "):
            direction = command[3:]
            if direction in room["exits"]:
                current_location = room["exits"][direction]
                print(f"You walk {direction}...")
            else:
                print("You can't go that way.")
        elif command == "look":
            print(room["description"])
        elif command == "inventory":
            player.view_inventory()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")

def main():
    player = create_character()
    player.display_stats()
    intro_scene(player)
    explore_world(player)


if __name__ == "__main__":
    main()