import random
import json


from entities import Monster, monster_data


def create_random_monster():
    name = random.choice(list(monster_data.keys()))
    attributes = monster_data[name]
    return Monster(name, attributes["HP"], attributes["atk"], attributes["dfs"])


# 게임의 메인 로직...


def main():
    player = Monster("Charmander")
    monster = create_random_monster()

    print(f"A wild {monster.name} appears!")
    print("\nPo: attack, quit")
    command = input("Enter your pokemon: ").strip().lower()

    while player.is_alive() and monster.is_alive():
        print("\nCommands: attack, quit")
        command = input("Enter your command: ").strip().lower()

        if command == "attack":
            player.attack(monster)
            if monster.is_alive():
                monster.attack(player)
        elif command == "quit":
            print("You fled the battle.")
            break
        else:
            print("Invalid command.")

        print(f"\nPlayer Health: {player.HP}, Monster Health: {monster.HP}")

    if not player.is_alive():
        print("You were defeated.")
    elif not monster.is_alive():
        print("You defeated the monster!")


if __name__ == "__main__":
    main()
