import time
import random #IMPORT A RANDOM MODULE (DICE ROLL)
import turtle

#DEFINE A PLAYER CLASS TO SCORE PLAYER INFORMATION
class Player:
    def __init__(self, name):
        self.health = 100
        self.weapon = None
        self.armor = 0
        self.health_potions = 3
        self.name = name

#DEFINE A CREATURE CLASS FOR ENEMIES
class Creature:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class NPC:
    def __init__(self, name, profession, dialogue):
        self.name = name
        self.profession = profession
        self.dialogue = dialogue

    def talk(self):
        print(f"{self.name}: {self.dialogue}")

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

class Weapon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

def display_text(text, delay = 5):
    turtle.clear() #CLEAR THE SCREEN BEFORE DISPLAYING NEW TEXT
    turtle.write(text, align="center", font=("Public Pixel", 16,"normal"))
    time.sleep(delay)

def intro():
    #TALK OF A LEGEND
    display_text("Welcome to the Extended Text Adventure Game!")
    time.sleep(3)
    display_text(input("Enter a name of your character: "))
    time.sleep(3)
    display_text(f"Welcome {player.name}")
    #HELP DEFINE CODE FOR THE NAME
    

def make_choice(choices):
    display_text("Choose your path:")
    choice_text = ""
    for i, choice in enumerate(choices, start=1):
        choice_text += f"{i}. {choice}\n"
    display_text(choice_text)

    return int(turtle.textinput("Input", "Enter the number of your choice: "))

def use_health_potion(player):
    if player.health_potions > 0:
        player.health += random.randint(20, 30) #RESTORE A RANDOM AMOUNT OF HEALTH
        player.health_potions -= 1
        display_text("You used a health potion and restored some health.")
        display_text(f"Current health: {player.health}")
        display_text(f"Remaining health potions: {player.health_potions}")
    else:
        display_text("You do not have any health potions left.")

def equip_armor(player, found_armor):
    display_text(f"You found {found_armor.name}!\nDo you want to equip it?\n1. Yes\n2. No")
    choice = int(turtle.textinput("Input", "Enter the number of your choice: "))

    if choice == 1:
        player.armor = found_armor.defense
        display_text(f"You equipped {found_armor.name}.")
    else:
        display_text(f"You chose not to equip {found_armor.name}.")

def town(player):
    """This function defines town in which the player starts their journey"""
    display_text("You find yourself in a small town")
    time.sleep(3)
    display_text("You realize you're at its square")
    time.sleep(3)
    choice = make_choice(["Look around", "Go to tavern"])

    if choice == 1:
        display_text("You decide to look around")
        time.sleep(3)
        display_text("You see a potionshop")
        time.sleep(3)
        display_text("Do you wish to go in?")
        time.sleep(3)
        choice = make_choice(["Approach", "Keep looking"])

        if choice == 1:
            #def potion_shop(player):
                #"""This function describes potionshop in town"""
            display_text("As you come close you see a small shop")
            time.sleep(3)
            display_text("It's made of stone and has a small sign above")
            time.sleep(3)
            display_text("The sign says 'Luciu's potion shop")
            time.sleep(3)
            display_text("You go in")
            time.sleep(3)
            display_text("The shop is empty")
            time.sleep(3)
            display_text("You see a bell at the counter")
            time.sleep(3)
            display_text("Do you wish to ring or continue looking around?")
            time.sleep(3)
            choice = make_choice(["Ring", "Keep looking around"])

            if choice == 1:
                display_text("You ring the bell and an elderly man appears at the counter")
                time.sleep(3)
                display_text("He asks: 'Hello, how may I help you?'")
                time.sleep(3)
                display_text("You tell him you're in need of some healing items")
                time.sleep(3)
                display_text("He says: 'I do have those, healing potions'")
                time.sleep(3)
                display_text("He adds: 'Three for one gold coin'")
                time.sleep(3)
                display_text("You only need one and you ask him if he could sell you only one")
                time.sleep(3)
                display_text("He answers: 'Take it for free, you seem like a hero in need'")
                time.sleep(3)
                display_text("You thank him and leave the shop")
                #ADD POTION
                time.sleep(3)
                display_text("Leaving the potion shop you notice a forge across the square")
                time.sleep(3)
                choice = make_choice(["Go in", "Go straight to tavern"])

                if choice == 1:
                    display_text("You come to the small forge")
                    time.sleep(3)
                    display_text("The sign above the entrance says: 'Gordon's forge'")
                    time.sleep(3)
                    display_text("You go in and find a large man working on some kind of weapon")
                    time.sleep(3)
                    display_text("You greet him, however, he seems to be occupied")
                    choice = make_choice(["Speak louder", "Wait"])

                    if choice == 1:
                        display_text("You raise your voice and the man turns around")
                        time.sleep(3)
                        display_text("He asks: 'What do you need?'")
                        time.sleep(3)
                        display_text("You ask whether he has some equipment that could of a use to your journey")
                        time.sleep(5)
                        display_text("He replies: 'Of course, best in town are my swords and daggers!\n Do you wish to purchase some?'")
                        time.sleep(5)
                        choice = make_choice(["Purchase equipment", "Refuse the offer"])

                        if choice == 1:
                            time.sleep(5)
                            display_text("He replies: 'Of course, best in town are my swords and daggers!\n Do you wish to purchase some?'")
                            choice = make_choice(["Purchase a sword", "Purchase a dagger"])

                            if choice == 1:
                                display_text("You decide to purchase a sword which costs you 1 gold coin")
                                #PAY 1 GOLD COIN + ADD AN OPTION NOT ENOUGH GOLD
                    
                            else:
                                display_text("You decide to purchase a dagger which costs you 2 gold coins")
                                #PAY 2 GOLD COINS + ADD AN OPTION NOT ENOUGH GOLD

                    else:
                        display_text("You say you do not want to purchase anything at all")
                        time.sleep(3)
                        display_text("The swordsman looks at you unpleasantly")
                        time.sleep(3)
                        display_text("He raises his voice: 'Do not waste my precious time then'")
                        time.sleep(3)
                        display_text("That remark angers you and you decide to leave the forge")
                        return True
                
                else:
                    display_text("You wait for about ten minutes when you realize there is no point in waiting")
                    time.sleep(3)
                    display_text("Disappointed you leave the forge and head for the local tavern")
                    return True
                
            else:
                display_text("You see a small wooden box at the corner of the room")
                time.sleep(3)
                display_text("You open it and nothing happens")
                time.sleep(3)
                display_text("That seems to disappoint you")
                time.sleep(3)
                display_text("You decide to leave the shop")
                time.sleep(3)
                display_text("All the sudden you feel heavier")
                time.sleep(3)
                display_text("You look into your backpack")
                time.sleep(3)
                display_text("Three health potions in your inventory")
                #ADD THREE POTIONS
                time.sleep(3)
                display_text("Leaving the potion shop you notice a forge across the square")
                time.sleep(3)
                choice = make_choice(["Go in", "Go straight to tavern"])

                if choice == 1:
                    display_text("You come to the small forge")
                    time.sleep(3)
                    display_text("The sign above the entrance says: 'Gordon's forge'")
                    time.sleep(3)
                    display_text("You go in and find a large man working on some kind of weapon")
                    time.sleep(3)
                    display_text("You greet him, however, he seems to be occupied")
                    choice = make_choice(["Speak louder", "Wait"])

                    if choice == 1:
                        display_text("You raise your voice and the man turns around")
                        time.sleep(3)
                        display_text("He asks: 'What do you need?'")
                        time.sleep(3)
                        display_text("You ask whether he has some equipment that could of a use to your journey")
                        time.sleep(5)
                        choice = make_choice(["Purchase equipment", "Refuse the offer"])

                        if choice == 1:
                            time.sleep(5)
                            display_text("He replies: 'Of course, best in town are my swords and daggers!\n Do you wish to purchase some?'")
                            choice = make_choice(["Purchase a sword", "Purchase a dagger"])

                            if choice == 1:
                                display_text("You decide to purchase a sword which costs you 1 gold coin")
                                #PAY 1 GOLD COIN + ADD AN OPTION NOT ENOUGH GOLD
                    
                            else:
                                display_text("You decide to purchase a dagger which costs you 2 gold coins")
                                #PAY 2 GOLD COINS + ADD AN OPTION NOT ENOUGH GOLD

                    else:
                        display_text("You say you do not want to purchase anything at all")
                        time.sleep(3)
                        display_text("The swordsman looks at you unpleasantly")
                        time.sleep(3)
                        display_text("He raises his voice: 'Do not waste my precious time then'")
                        time.sleep(3)
                        display_text("That remark angers you and you decide to leave the forge and head for the local tavern")
                        return True
                
                else:
                    display_text("You wait for about ten minutes when you realize there is no point in waiting")
                    time.sleep(3)
                    display_text("Disappointed you leave the forge and head for the local tavern")
                    return True
                
        else:
            display_text("You decide to keep looking around")
            time.sleep(3)
            display_text("All the sudden you notice forge")
            time.sleep(3)
            choice = make_choice(["Go in", "Keep looking around"])

            if choice == 1:
                display_text("You come to a small forge")
                time.sleep(3)
                display_text("The sign above the entrance says: 'Gordon's forge'")
                time.sleep(3)
                display_text("You go in and find a large man working on some kind of weapon")
                time.sleep(3)
                display_text("You greet hi, however, he seems to be occupied")
                choice = make_choice(["Speak louder", "Wait"])

                if choice == 1:
                    display_text("You raise your voice and the man turns around")
                    time.sleep(3)
                    display_text("He asks: 'What do you need?'")
                    time.sleep(3)
                    display_text("You ask whether he has some equipment that could of a use to your journey")
                    time.sleep(5)
                    choice = make_choice(["Purchase equipment", "Refuse the offer"])

                    if choice == 1:
                        time.sleep(5)
                        display_text("He replies: 'Of course, best in town are my swords and daggers!\n Do you wish to purchase some?'")
                        choice = make_choice(["Purchase a sword", "Purchase a dagger"])


                        if choice == 1:
                            display_text("You decide to purchase a sword which costs you 1 gold coin")
                            #PAY 1 GOLD COIN + ADD AN OPTION NOT ENOUGH GOLD
                    
                        else:
                            display_text("You decide to purchase a dagger which costs you 2 gold coins")
                            #PAY 2 GOLD COINS + ADD AN OPTION NOT ENOUGH GOLD

                else:
                    display_text("You say you do not want to purchase anything at all")
                    time.sleep(3)
                    display_text("The swordsman looks at you unpleasantly")
                    time.sleep(3)
                    display_text("He raises his voice: 'Do not waste my precious time then'")
                    time.sleep(3)
                    display_text("That remark angers you and you decide to leave the forge")
                    return True
                
            else:
                display_text("You wait for about ten minutes when you realize there is no point in waiting")
                time.sleep(3)
                display_text("Disappointed you leave the forge")
                return True

    else:
        display_text("You decide to head straight for the tavern")
        time.sleep(3)
        return True

def tavern(player):
    """This function defines the local tavern"""
    display_text("You find yourself before the doors to the tavern")
    time.sleep(3)
    display_text("You go in")
    time.sleep(3)
    display_text("It is crowded, tables are filled as if feasts were of no price")
    time.sleep(3)
    display_text("You decide to sit down")
    time.sleep(3)
    display_text("In the corner of the room you see only free place")
    time.sleep(3)
    display_text("As you approach you notice a small hooded man sitting there")
    time.sleep(3)
    display_text("He also takes notice of you and invites to you to sit with him")
    time.sleep(3)
    choice = make_choice(["Sit with the mysterious man", "Keep looking for a free spot"])

    if choice == 1:
        display_text("You come to the table and greet the man")
        time.sleep(3)
        display_text("He asks: 'What is your name?'")
        time.sleep(3)
        display_text(f"You answer {player.name}")
        time.sleep(3)
        display_text("He adds: 'My name is Siril, it is my pleasure to meet you traveler'")
        time.sleep(3)
        display_text("You ask about the legend that brought you here")
        time.sleep(3)
        display_text("He says: 'I do know of that'")
        time.sleep(3)
        display_text("You ask whether he knows how to get to the castle of the legend")
        time.sleep(3)
        display_text("He replies: 'Of course'")
        time.sleep(3)
        display_text("The man then continues to give you the instructions to the location")
        time.sleep(3)
        display_text("You thank the man and offer to drink with him")
        time.sleep(3)
        display_text("He agrees and you two spend the evening together")
        time.sleep(3)
        display_text("After the man takes his leave you ask the barmaid for a free room")
        time.sleep(3)
        display_text("She tells you there is one in the attic")
        time.sleep(3)
        display_text("You take it and sleep through the night")
        time.sleep(3)
        display_text("In the morning you head straight for the forest to waist no time")
        time.sleep(3)

    else:
        display_text("As there seems to be no other table you free you come back and sit with the man")
        time.sleep(3)
        display_text("You come to the table and greet the man")
        time.sleep(3)
        display_text("He asks: 'What is your name?'")
        time.sleep(3)
        display_text(f"You answer {player.name}")
        time.sleep(3)
        display_text("He adds: 'My name is Siril, it is my pleasure to meet you traveler'")
        time.sleep(3)
        display_text("You ask about the legend that brought you here")
        time.sleep(3)
        display_text("He says: 'I do know of that'")
        time.sleep(3)
        display_text("You ask whether he knows how to get to the castle of the legend")
        time.sleep(3)
        display_text("He replies: 'Of course'")
        time.sleep(3)
        display_text("The man then continues to give you the instructions to the location")
        time.sleep(3)
        display_text("You thank the man and offer to drink with him")
        time.sleep(3)
        display_text("He agrees and you two spend the evening together")
        time.sleep(3)
        display_text("After the man takes his leave you ask the barmaid for a free room")
        time.sleep(3)
        display_text("She tells you there is one in the attic")
        time.sleep(3)
        display_text("You take it and sleep through the night")
        time.sleep(3)
        display_text("In the morning you head straight for the forest to waist no time")
        time.sleep(3)
                    
def forest_path(player):
    """This function represents the players way through the forest, offering choices and paths"""
    display_text("You start walking on a narrow path through the forest.\nSuddenly, you encounter a fork in the road.")
    choice = make_choice(["Take the left path", "Take the righ path"])

    if choice == 1:
        display_text("You chose to take the left path.\nAs you walk, you encounter a friendly squirrel.\nThe squirrel guides you to a shortcut.")
        return True
    else:
        display_text("You chose to take the right path.\nYou encounter a group of agressive wolves.\nYou manage to scare them away using a loud noise.")
        #PLAYER COLLECTS A BASIC WEAPON AFTER SCARING AWAY WOLVES
        player.weapon = "Wooden Sword"
        display_text(f"You found a {player.weapon}.")
        return True

def battle(player, enemy):
    display_text(f"You encounter a {enemy.name}!")
    time.sleep(5)

    while player.health > 0 and enemy.health > 0:
        display_text("\nPlayer Stats:")
        display_text(f"Health: {player.health}")
        display_text(f"Weapon: {player.weapon}")
        display_text(f"Armor: {player.armor}")
        display_text(f"Health Potions: {player.health_potions}")

        display_text(f"\n{enemy.name} Stats:")
        display_text(f"Health: {enemy.health}")
        display_text(f"Damage: {enemy.damage}")

        attack_choice = make_choice(["Attack", "Run", "Use health potion"])

        if attack_choice == 1:
            """ Player attacks the enemy"""
            player_attack = random.randint(5, 15)
            enemy.health -= player_attack
            display_text(f"You attack the {enemy.name} and deal {player_attack} damage!")

            #ENEMY ATTACKS THE PLAYER
            enemy_attack = random.randint(5, 15)
            player.health -= max(0, enemy_attack - player.armor)
            display_text(f"The {enemy.name} attacks you and deals {max(0, enemy_attack - player.armor)} damage!")
        elif attack_choice == 2:
            display_text(f"You try to run from the {enemy.name}, but it catches you!")
            enemy_attack = random.randint(10, 20)
            player.health -= max(0, enemy_attack - player.armor)
            display_text(f"The {enemy.name} attacks you and deals {max(0, enemy_attack - player.armor)} damage!")
        else:
            use_health_potion(player)

    if player.health <= 0:
        display_text("You have been defeated...\nGame over!")
        exit()
    else:
        display_text(f"You defeated the {enemy.name}!")
        
        if enemy.name == "Giant Spider" and random.choice([True, False]):
            bronze_sword = Weapon("Bronze Sword", 15)
            display_text(f"The {enemy.name} dropped a {bronze_sword.name} with double the attack stats!")
            display_text(f"You found a {bronze_sword.name}.")
            player.weapon = bronze_sword.name
            
        return True
            
def cave(player):
    """Function that represents a cave a player can interact with"""
    display_text("You arrive at the entrance of a dark cave.")
    time.sleep(3)
    display_text("It seems to be the only way to reach the treasure.")
    time.sleep(3)

    while True:
        display_text("As you enter the cave, you hear strange noises.")
        time.sleep(3)
        display_text("You see two tunnels: one on the left and one on the right.")
        time.sleep(3)
        choice = make_choice(["Enter the left tunnel", "Enter the right tunnel"])

        if choice == 1:
            display_text("You chose to enter the left tunnel.")
            time.sleep(3)
            display_text("You encounter a giant spider!")
            #COMBAT WITH THE GIANT SPIDER
            giant_spider = Creature("Giant spider", 40, 15)
            if not battle(player, giant_spider):
                display_text("You need to find the correct path in the cave to reach the treasure.\nTry again!")
                continue
        else:   
            display_text("You chose to enter the right tunnel.")
            time.sleep(3)
            display_text("The tunnel leads to a dead end. You backtrack to the entrance.")
            time.sleep(3)
            display_text("You need to find the correct path in the cave to reach the treasure. Try again.")
            continue

        next_choice = make_choice(["Continue through the cave", "Leave the cave"])
    
        if next_choice == 1:
            display_text("You continue through the cave")
            ogre = Creature("Ogre", 60, 20)
            if not battle(player, ogre):
                display_text("You need to find the correct path in the cave to reach the treasure.\n Try again!")
                continue

            found_armor = Armor("Steel Armor", 10)
            equip_armor(player, found_armor)

            next_choice = make_choice(["Go deeper into the cave", "Leave the cave"])

            if next_choice == 1:
                display_text("You decide to go deeper into the cave.")
                dragon = Creature("Dragon", 80, 25)
                if not battle(player, dragon):
                    display_text("You need to find the correct path in the cave to reach the treasure.\nTry again!")
                    continue
                else:
                    next_choice = make_choice(["Go deeper into  the cave", "Leave the cave"])
                    if next_choice == 1:
                        display_text("You go deeper into the cave.")
                        treasure_room(player)
                        return True
                    else:
                        display_text("You leave the cave without reaching the treasure")
                        return False
            else:
                display_text("You leave the cave without reaching the treasure")
                return False
        else:
            display_text("You leave the cave without reaching the treasure")
            return False

def treasure_room(player):
    display_text("Congratulations! You have reached the treasure room.")
    time.sleep(3)
    display_text("You open the treasure chest and find a pile of gold and jewels.")
    time.sleep(3)
    display_text("You have successfully completed the adventure.")

if __name__ == "__main__":
    turtle.setup(width=800, height=600)
    turtle.bgcolor("red")
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()

    intro()

    player = Player()

    if forest_path(player):
        cave(player)    

    input("Press Enter to exit...")
