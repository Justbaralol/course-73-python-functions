import time
import random #IMPORT A RANDOM MODULE (DICE ROLL)

#DEFINE A PLAYER CLASS TO SCORE PLAYER INFORMATION
class Player:
    def __init__(self):
        self.health = 100
        self.weapon = None
        self.armor = None

#DEFINE A CREATURE CLASS FOR ENEMIES
class Creature:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

#CREATE INSTANCES OF THE PLAYER AND CREATURES
player = Player()
wolf = Creature("Wolf", 30, 10)
giant_spider = Creature("Giant Spider", 40, 15)

def intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1) #ADDS A PAUSE AND THE TEXT LINES GENERATE AFTER ONE SECOND
    print("You find yourself in a dark and mysterious forest.")
    time.sleep(1)
    print("Your goal is to reach the treasure hidden deep within.")
    time.sleep(1)
    print("Be careful, as the forest is filled with dangers.")
    time.sleep(1)

def make_choice(choices):
    """Function that takes a list of choices as an argument"""
    print("Choose your path")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter a number of your choice: "))
            if i <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    """This function represents the players way through the forest, offering choices and paths"""
    print("You start walking on a narrow path through the forest.")
    time.sleep(1)
    print("Suddenly, you encounter a fork in the road.")
    time.sleep(1)
    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        print("You chose to take the left path.")
        time.sleep(1)
        print("As you walk, you encounter a friendly squirrel.")
        time.sleep(1)
        print("The squirrel guides you to a shortcut.")
        return True
    else:
        print("You chose to take the right path.")
        time.sleep(1)
        print("You encounter a group of agressive wolves.")
        time.sleep(1)
        print("You manage to scare them away using a loud noise.")
        #PLAYER COLLECTS A BASIC WEAPON AFTER SCARING AWAY WOLVES
        player.weapon = "Wooden Sword"
        print(f"You found a {player.weapon}.")
        return True

def cave():
    """Function that represents a cave a player can interact with"""
    print("You arrive at the entrance of a dark cave.")
    time.sleep(1)
    print("It seems to be the only way to reach the treasure.")
    time.sleep(1)

    while True:
        print("As you enter the cave, you hear strange noises.")
        time.sleep(1)
        print("You see two tunnels: one on the left and one on the right.")
        time.sleep(1)
        choices = ["Enter the left tunnel", "Enter the right tunnel"]
        choice = make_choice(choices)

        if choice == 1:
            print("You chose to enter the left tunnel.")
            time.sleep(1)
            print("You encounter a giant spider!")
            #COMBAT WITH THE GIANT SPIDER
            combat(giant_spider)
            return True
        else:   
            print("You chose to enter the right tunnel.")
            time.sleep(1)
            print("The tunnel leads to a dead end. You backtrack to the entrance.")
            print("You need to find the correct path in the cave to reach the treasure. Try again.")
            #return False

def treasure_room():
    print("Congratulations! You have reached the treasure room.")
    time.sleep(1)
    print("You open the treasure chest and find a pile of gold and jewels.")
    time.sleep(1)
    print("You have successfully coompleted the adventure.")

def combat(enemy):
    print(f"You are in combat with a {enemy.name}!")

    while player.health > 0 and enemy.health > 0:
        print("\nPlayer Stats:")
        print(f"Health: {player.health}")
        print(f"Weapon: {player.weapon}")

        print(f"\n{enemy.name} Stats:")
        print(f"Health: {enemy.health}")
        print(f"Damage: {enemy.damage}")

        attack_choice = make_choice(["Attack", "Run"]) #YOU CAN ADD OPTION LIKE USE A POTION OR A SPELL

        if attack_choice == 1:
            #PLAYER ATTACKS THE ENEMY
            player_attack = random.randit(5, 15)
            enemy.health -= player_attack
            print(f"You attack the {enemy.name} and deal {player_attack} damage!")

            #ENEMY ATTACKS THE PLAYER
            enemy_attack = random.randit(5, 15)
            player.health -= enemy_attack
            print(f"The {enemy.name} attacks you and deals {enemy_attack} damage!")
        else:
            print(f"You try to run from the {enemy.name}, but it catches you!")
            enemy_attack = random.randit(10, 20)
            player.health -= enemy_attack
            print(f"The {enemy.name} attacks you and deals {enemy_attack} damage!")

    if player.health <= 0:
        print("You have been defeated.")
        time.sleep(1)
        print("Game over!")
    else:
        print(f"You defeated the {enemy.name}!")

if __name__ == "__main__":
    intro()

    if forest_path():
        while not cave():
            pass #LOOP UNTIL THE PLAYER FINDS THE CORRECT PATH IN THE CAVE

        treasure_room()

    input("Press Enter to exit...")
