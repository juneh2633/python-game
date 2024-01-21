import random
import json


from classes.entities import Monster
from module import monster_manㄴage as mm


def main():
    monster = mm.create_monster("random")
    monster_data = mm.load_monster_data()

    message = "******Choose your pokemon****** \n" + ", ".join(
        f"({i})" for i in monster_data
    )
    print(f"A wild {monster.name} appears!")
    print(message)
    command = input("Enter your pokemon: ").strip()
    player = mm.create_monster(command)
    available_skills = [monster.skill1_name, monster.skill2_name, monster.skill3_name]

    while player.is_alive() and monster.is_alive():
        turn = 0
        while turn == 0:
            print(f"\n HP: {player.HP}, pp: {player.pp}")
            print(f"\n enemy: HP: {monster.HP}")
            print(
                f"\nCommands: 1:{player.skill1_name},2: {player.skill2_name}, 3: {player.skill3_name} quit"
            )
            command = input("Enter your command: ").strip()
            if command == "1":
                player.use_skill(player.skill1_name, monster)
                if monster.is_alive():
                    selected_skill = random.choice(available_skills)
                    monster.use_skill(selected_skill, player)
                turn = 1
            elif command == "2":
                player.use_skill(player.skill2_name, monster)
                if monster.is_alive():
                    selected_skill = random.choice(available_skills)
                    monster.use_skill(selected_skill, player)
                turn = 1
            elif command == "3":
                player.use_skill(player.skill3_name, monster)
                if monster.is_alive():
                    selected_skill = random.choice(available_skills)
                    monster.use_skill(selected_skill, player)
                turn = 1
            elif command == "quit":
                turn = 1
                player.HP = 0
                print("You fled the battle.")
                break
            else:
                print("Invalid command.")

        print(f"\nPlayer HP: {player.HP}, Monster HP: {monster.HP}")

    if not player.is_alive():
        print("You were defeated.")
    elif not monster.is_alive():
        print("You defeated the monster!")


if __name__ == "__main__":
    main()
