import random

class Player:
    def __init__(self, name, gender, health, level=1, damage=5, reach=1, defence=0):
        self.name = name
        self.gender = gender
        self.health = health
        self.level = level
        self.damage = damage
        self.reach = reach
        self.defence = defence

    def __repr__(self):
        return """
        This is your player statics:
        Name: {name}
        Health: {health}
        Level: {level}
        Damage: {damage}
        Range: {reach}
        Defence: {defence}
        """



class Weapon:
    def __init__(self, weapon, damage, reach, defence):
        self.weapon = weapon
        self.damage = damage
        self.reach = reach
        self.defence = defence

    def __repr__(self):
        return "{weapon}: {damage} Damage, {reach} Range, {defence} Defence".format(weapon=self.weapon, damage=str(self.damage), reach=str(self.reach), defence=str(self.defence))

behnam = Player("Behnam", "M", 120)
bryar = Player("Bryar", "F", 96)


player_name = input("Choose your character name: ")
player_gender = (input("""Females are faster by %50 but has %20 less health than men. Choose your gender carefully!
Enter M for Male or F for Female: """).upper())
correct_gender = False
while not correct_gender:
    if player_gender == "M":
        correct_gender = True
    elif player_gender == "F":
        correct_gender = True
    else: 
        print("Invalid input. Only enter M or F.")

if player_gender == "M":
    player_health = 120
elif player_gender == "F":
    player_health = 96

player = Player(player_name, player_gender, player_health)

sword = Weapon("Sword", 12, 1, 1)
spear = Weapon("Spear", 10, 3, 3)
bow = Weapon("Bow", 11, 4, 0)
shield = Weapon("Shield", 5, 1, 8)

player_weapon1 = int(input("""
List of weapons:
1. {sword}
2. {spear}
3. {bow}
4. {shield}

Enter your main weapon with its number (1, 2 , 3, or 4): 
""".format(sword=sword, spear=spear, bow=bow, shield=shield)))
player_weapon2 = int(input("Enter your secondary weapon: "))

if player_weapon1 == 1: 
    player_weapon1 = sword
elif player_weapon1 == 2:
    player_weapon1 = spear
elif player_weapon1 == 3:
    player_weapon1 = bow
elif player_weapon1 == 4:
    player_weapon1 = shield

if player_weapon2 == 1: 
    player_weapon2 = sword
elif player_weapon2 == 2:
    player_weapon2 = spear
elif player_weapon2 == 3:
    player_weapon2 = bow
elif player_weapon2 == 4:
    player_weapon2 = shield

player_main = Player(player.name, player.gender, player.health)
player_main.damage += player_weapon1.damage
player_main.defence += player_weapon1.defence
player_main.reach += player_weapon1.reach

player_secondary = Player(player.name, player.gender, player.health)
player_secondary.damage += player_weapon2.damage
player_secondary.defence += player_weapon2.defence
player_secondary.reach += player_weapon2.reach


print("""{name}({gender}{level}), You have {health} health left. This is your statics with your main weapon: 
Damage: {damage}
Range: {reach}
Defence: {defence}

And this is your statics with your secondary weapon: 
Damage: {damage2}
Range: {reach2}
Defence: {defence2}
""".format(name=player.name, gender=player.gender, level=player.level, health=player.health, damage=player_main.damage, reach=player_main.reach, defence=player_main.defence, damage2=player_secondary.damage, reach2=player_secondary.reach, defence2=player_secondary.defence))
