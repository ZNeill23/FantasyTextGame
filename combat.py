# combat.py

import random

def start_combat(player, enemy):
    print(f"\nYou are attacked by a {enemy['name']}!")

    while player.hp > 0 and enemy['hp'] > 0:
        print(f"\nYour HP: {player.hp}")
        print(f"{enemy['name']}'s HP: {enemy['hp']}")
        print("What will you do?")
        print("1. Attack")
        print("2. Flee")

        action = input("> ")

        if action == "1":
            # Player attacks
            damage = random.randint(5, 10) + player.strength
            enemy['hp'] -= damage
            print(f"You strike the {enemy['name']} for {damage} damage!")
        elif action == "2":
            print("You run away safely!")
            return False
        else:
            print("Invalid action.")
            continue

        if enemy['hp'] > 0:
            # Enemy attacks
            enemy_damage = random.randint(3, 8)
            player.hp -= enemy_damage
            print(f"The {enemy['name']} hits you for {enemy_damage} damage!")
    
    if player.hp > 0:
        print(f"\nYou defeated the {enemy['name']}!")
        return True
    else:
        print(f"\nYou were slain by the {enemy['name']}...")
        print("Game over.")
        exit()