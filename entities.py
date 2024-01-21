import random
import json


def load_skill_data():
    with open("skills.json", "r") as file:
        data = json.load(file)
    return data


skill_data = load_skill_data()


class Monster:
    def __init__(self, name, HP, atk, dfs, spd, atk_type, skill1, skill2, skill3):
        self.name = name
        self.HP = HP
        self.pp = 100
        self.atk = atk
        self.dfs = dfs
        self.spd = spd
        self.atk_type = atk_type
        self.skill1_name = skill1
        self.skill2_name = skill2
        self.skill3_name = skill3
        self.skill1 = skill_data[skill1]
        self.skill2 = skill_data[skill2]
        self.skill3 = skill_data[skill3]

        def use_skill(self, skill, target):
            skill_info = getattr(self, skill)
            self.pp -= skill_info["pp"]
            if random.randint(1, 100) <= skill_info["accuracy_rate"]:
                damage = skill_info["power"] * (atk + 100) / 100
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
