# world.py

world_map = {
    "Dunwich": {
        "description": "You are in the peaceful village of Dunwich. The tavern is to the west. A forest lies to the north.",
        "exits": {"north": "Forest", "west": "Tavern"}
    },
    "Tavern": {
        "description": "You are inside the lively tavern. Locals chat over drinks. The village is to the east.",
        "exits": {"east": "Dunwich"}
    },
    "Forest": {
        "description": "The trees are thick here, and shadows move between them. Danger could be near. The village is to the south.",
        "exits": {"south": "Dunwich"}
    }
}