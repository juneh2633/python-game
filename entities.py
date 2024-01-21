import random
import json


def load_skill_data():
    with open("json/skills.json", "r") as file:
        data = json.load(file)
    return data


skill_data = load_skill_data()


def load_monster_data():
    with open("json/monsters.json", "r") as file:
        data = json.load(file)
    return data


class Monster:
    def __init__(self, name):
        monster_data = load_monster_data()
        stat = monster_data[name]
        self.name = name
        self.HP = stat["HP"]
        self.pp = 100
        self.atk = stat["atk"]
        self.dfs = stat["dfs"]
        self.spd = stat["spd"]
        self.atk_type = stat["atk_type"]
        self.skill1_name = stat["skill1"]
        self.skill2_name = stat["skill2"]
        self.skill3_name = stat["skill3"]
        self.skill4_name = "발버둥"
        self.skill1 = skill_data[self.skill1_name]
        self.skill2 = skill_data[self.skill2_name]
        self.skill3 = skill_data[self.skill3_name]
        self.skill4 = skill_data["발버둥"]

        def use_skill(self, skill, target):
            skill_info = getattr(self, skill)
            self.pp -= skill_info["pp"]
            if random.randint(1, 100) <= skill_info["accuracy_rate"]:
                damage = skill_info["power"] * (self.atk + 100) / 100
                target.HP -= damage * target.dfs / 100

                if skill_info["type"] == "deberf":
                    if skill_info["deberf"] == "atk":
                        target.atk += skill_info["deberf"]["atk"]
                    elif skill_info["debef"] == "dfs":
                        target.dfs += skill_info["deberf"]["dfs"]
                    print(
                        f"{self.name} uses {skill_info['name']} on {target.name} for deberf!"
                    )
                else:
                    print(
                        f"{self.name} uses {skill_info['name']} on {target.name} for {damage} damage!"
                    )
            else:
                print(f"{self.name}'s {skill_info['name']} missed!")

    def is_alive(self):
        return self.HP > 0
