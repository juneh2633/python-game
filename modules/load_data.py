import json


def load_skill_data():
    with open("json/skills.json", "r") as file:
        data = json.load(file)
    return data


def load_monster_data():
    with open("json/monsters.json", "r") as file:
        data = json.load(file)
    return data


def load_type_data():
    with open("json/type.json", "r") as file:
        data = json.load(file)
    return data
