import random
import json


from classes.entities import Monster
from modules import monster_manage as mm
from modules.fight import fight


def main():
    monster = mm.create_monster("random")
    monster_data = mm.load_monster_data()

    message = "******Choose your pokemon****** \n" + ", ".join(
        f"[{i}, 타입: {monster_data[i]['atk_type']}]" for i in monster_data
    )
    print("************************************ㄴ*********")
    print(f"야생의 {monster.name}가 나타났다!")
    print(message)
    check = 0
    player = mm.create_monster("random")
    while check == 0:
        command = input("Enter your pokemon: ").strip()
        player = mm.create_monster(command)
        if player == False:
            print("Invalid command.")
        else:
            check = 1

    available_skills = [monster.skill1_name, monster.skill2_name, monster.skill3_name]

    while player.is_alive() and monster.is_alive():
        turn = 0
        while turn == 0:
            print("*********************************************")
            print(f"* HP: {player.HP:.2f}, pp: {player.pp}")
            print(f"*enemy: HP: {monster.HP:.2f}")
            print("*********************************************")
            print(
                f"\nCommands: 1:{player.skill1_name},2: {player.skill2_name}, 3: {player.skill3_name} 4: 도망가기"
            )
            command = input("Enter your command: ").strip()
            if monster.pp <= 0:
                available_skills = [monster.skill4_name]
            monster_skill = random.choice(available_skills)
            player_skill = player.skill4_name
            if command == "4":
                turn = 1
                player.HP = 0
                print("You fled the battle.")
                break
            elif player.pp <= 0:
                print("pp가 없어 발버둥을 했다.")
                player_skill = player.skill4_name
                fight(player, monster, player.skill)
                turn = 1
            elif command == "1":
                player_skill = player.skill1_name
                turn = 1
            elif command == "2":
                player_skill = player.skill2_name
                turn = 1
            elif command == "3":
                player_skill = player.skill3_name
                turn = 1
            else:
                print("Invalid command.")
            fight(player, monster, player_skill, monster_skill)
    if not player.is_alive():
        print("졌다!")
    elif not monster.is_alive():
        print("이겼다!")


if __name__ == "__main__":
    main()
