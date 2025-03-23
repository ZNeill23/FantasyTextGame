# scenes/intro.py

def intro_scene(player):
    print(f"\nWelcome, {player.name} the {player.char_class}, to the realm of Eldoria!")
    print("The sun rises over the sleepy village of Dunwich. Smoke curls from chimneys as you step out into the morning chill.")
    print("You're about to begin your first adventure.")

    while True:
        print("\nWhat woudld you like to do?")
        print("1. Visit the village tavern.")
        print("2. Head to the town gate and speak to the guard.")
        print("3. Explore the forest to the north.")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            print("\nYou push open the tavern door. The smell of ale and roasted meat hits you.")
            print("A grizzled man waves you over. 'You look like you can handle yourself,' he says. 'There's trouble brewing outside the walls.'")
            # We can branch to a quest hook or rumor system here later
            break
        elif choice == "2":
            print("\nThe guard at the gate looks bored. He straigtens as you approach.")
            print("'If you're looking to leave town, be careful,' he warns. 'Bandits have been spotted on the forest road.'")
            # This could trigger a world map later
            break
        elif choice == "3":
            print("\nYou follow a dirt path into dark woods. The trees close in around you.")
            print("You hear rustling... something is out there.")
            # This could lead into an encounter or combat scene
            break
        else:
            print("Invalid choice. Try again.")

    print("\n[End of demo scene - more to come!]")