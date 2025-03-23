# enemies.py

def get_enemy(enemy_type):
    if enemy_type == "goblin":
        return {
            "name": "Goblin",
            "hp": 20,
            "loot": "Rusty Sword",
            "xp": 50
        }
    elif enemy_type == "wolf":
        return {
            "name": "Wolf",
            "hp": 30,
            "loot": "Wolf Fang",
            "xp": 60
        }
    else:
        return None