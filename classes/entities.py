import random
import json
from modules.load_data import load_monster_data
from modules.load_data import load_skill_data
from modules.load_data import load_type_data

skill_data = load_skill_data()
monster_data = load_monster_data()
type_data = load_type_data()


class Monster:
    def __init__(self, name):
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

    def use_skill(self, skill_name, target):
        skill_info = skill_data[skill_name]
        self.pp -= skill_info["pp"]

        if random.randint(1, 100) <= skill_info["accuracy_rate"]:
            type_damage = type_data[skill_info["atk_type"]][target.atk_type]
            damage = (
                skill_info["power"]
                * (self.atk + 100 + random.randint(-3, 3))
                / 100
                * (type_damage)
            )
            target.HP -= damage * target.dfs / 100

            if skill_info["atk_type"] == "deberf":
                if skill_info["deberf"] == "atk":
                    target.atk += skill_info["deberf"]["atk"] + random.randint(-3, 3)
                elif skill_info["deberf"] == "dfs":
                    target.dfs += skill_info["deberf"]["dfs"]
                print(f"{self.name} uses {skill_name} on {target.name} for deberf!")
            else:
                print(
                    f"{self.name} uses {skill_name} on {target.name} for {damage * target.dfs / 100} damage!"
                )
        else:
            print(f"{self.name}'s {skill_name} missed!")

    def is_alive(self):
        return self.HP > 0


class Skill:
    def __init__(self, name):
        skill_data = load_skill_data()
