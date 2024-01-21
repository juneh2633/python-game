import random
import json


from entities import Monster


def load_monster_data():
    with open("json/monsters.json", "r") as file:
        data = json.load(file)
    return data


def create_monster(monster_name):
    if monster_name == "random":
        monster_data = load_monster_data()
        monster_name = random.choice(list(monster_data.keys()))

    return Monster(monster_name)


def main():
    monster = create_monster("random")
    monster_data = load_monster_data()

    message = "******Choose your pokemon****** \n" + ", ".join(
        f"({item})" for item in monster_data
    )
    print(f"A wild {monster.name} appears!")
    print(message)
    command = input("Enter your pokemon: ").strip()
    player = create_monster(command)

    while player.is_alive() and monster.is_alive():
        print(f"\n HP: {player.HP}, pp: {player.pp}")
        print(
            f"\nCommands: {player.skill1_name},{player.skill2_name}, {player.skill3_name} quit"
        )
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

        print(f"\nPlayer HP: {player.HP}, Monster HP: {monster.HP}")

    if not player.is_alive():
        print("You were defeated.")
    elif not monster.is_alive():
        print("You defeated the monster!")


if __name__ == "__main__":
    main()
