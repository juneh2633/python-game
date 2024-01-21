import random
import json
from classes.entities import Monster


def load_monster_data():
    with open("json/monsters.json", "r") as file:
        data = json.load(file)
    return data


def create_monster(monster_name):
    if monster_name == "random":
        monster_data = load_monster_data()
        monster_name = random.choice(list(monster_data.keys()))
    try:
        output_monster = Monster(monster_name)
        return Monster(monster_name)
    except KeyError as e:
        print(f"An error occurred: {e}")
        return False
