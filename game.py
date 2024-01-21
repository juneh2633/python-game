import random


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        damage = random.randint(10, 20)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, target):
        damage = random.randint(5, 15)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0


def create_random_monster():
    names = ["Charizard", "Bulbasaur", "Squirtle"]
    name = random.choice(names)
    health = random.randint(50, 100)
    return Monster(name, health)


def main():
    player = Player("Player 1")
    monster = create_random_monster()

    print(f"A wild {monster.name} appears!")

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

        print(f"\nPlayer Health: {player.health}, Monster Health: {monster.health}")

    if not player.is_alive():
        print("You were defeated.")
    elif not monster.is_alive():
        print("You defeated the monster!")


if __name__ == "__main__":
    main()
