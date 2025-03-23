# world.py

world_map = {
    "Dunwich": {
        "description": "You are in the peaceful village of Dunwich. The tavern is to the west. A forest lies to the north.",
        "exits": {"north": "Forest", "west": "Tavern"}
    },
    "Tavern": {
        "description": "You are inside the lively tavern. Locals chat over drinks. The village is to the east.",
        "exits": {"east": "Dunwich"},
        "npc": {
            "name": "Gregor the Grizzled",
            "dialogue": [
                "Ah, a fresh face! You looking for work?",
                "They say something stirs in the ancient ruins to the west...",
                "If you're brave, follow the road past the forest."
            ]
        }
    },
    "Forest": {
        "description": "The trees are thick here, and shadows move between them. Danger could be near. The village is to the south.",
        "exits": {"south": "Dunwich"},
        "enemy_spawn": "goblin"
    }
}