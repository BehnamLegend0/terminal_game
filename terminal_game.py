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


player_name = input("Player 1, Choose your character name: ")
player_gender = (input("""Females have %40 chance to do critical damage but has %25 less health than males. Choose your gender carefully!
Enter M for Male or F for Female: """).upper())
check = False
while not check:
    if player_gender == "M":
        check = True
    elif player_gender == "F":
        check = True
    else: 
        print("Invalid input. Only enter M or F.")

if player_gender == "M":
    player_health = 120
elif player_gender == "F":
    player_health = 90

player = Player(player_name, player_gender, player_health)


player2_name = input("Player 2, Choose your character name: ")
player2_gender = (input("""Females has %40 chance to do critical damage but has %25 less health than males. Choose your gender carefully!
Enter M for Male or F for Female: """).upper())
check = False
while not check:
    if player2_gender == "M":
        check = True
    elif player2_gender == "F":
        check = True
    else: 
        print("Invalid input. Only enter M or F.")

if player2_gender == "M":
    player2_health = 120
elif player2_gender == "F":
    player2_health = 90

player2 = Player(player2_name, player2_gender, player2_health)

sword = Weapon("Sword", 12, 1, 1)
spear = Weapon("Spear", 10, 3, 3)
bow = Weapon("Bow", 11, 4, 0)
shield = Weapon("Shield", 5, 1, 8)

check = False
while not check:
    player_weapon1 = int(input("""
    List of weapons:
    1. {sword}
    2. {spear}
    3. {bow}
    4. {shield}

    {player_name}, Enter your main weapon with its number (1, 2 , 3, or 4): 
    """.format(player_name=player_name, sword=sword, spear=spear, bow=bow, shield=shield)))
    if player_weapon1 in [1, 2, 3, 4]:
        check = True
    else:
        print("Invalid input. Enter 1, 2, 3, or 4!")

check = False
while not check:
    player_weapon2 = int(input("Enter your secondary weapon: "))
    if player_weapon2 in [1, 2, 3, 4]:
        check = True
    else:
        print("Invalid input. Enter 1, 2, 3, or 4!")


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

check = False
while not check:
    player2_weapon1 = int(input("""
    List of weapons:
    1. {sword}
    2. {spear}
    3. {bow}
    4. {shield}

    {player2_name}, Enter your main weapon with its number (1, 2 , 3, or 4): 
    """.format(player2_name=player2_name, sword=sword, spear=spear, bow=bow, shield=shield)))
    if player2_weapon1 in [1, 2, 3, 4]:
        check = True
    else:
        print("Invalid input. Enter 1, 2, 3, or 4!")

check = False
while not check:
    player2_weapon2 = int(input("Enter your secondary weapon: "))
    if player2_weapon2 in [1, 2, 3, 4]:
        check = True
    else:
        print("Invalid input. Enter 1, 2, 3, or 4!")


if player2_weapon1 == 1: 
    player2_weapon1 = sword
elif player2_weapon1 == 2:
    player2_weapon1 = spear
elif player2_weapon1 == 3:
    player2_weapon1 = bow
elif player2_weapon1 == 4:
    player2_weapon1 = shield

if player2_weapon2 == 1: 
    player2_weapon2 = sword
elif player2_weapon2 == 2:
    player2_weapon2 = spear
elif player2_weapon2 == 3:
    player2_weapon2 = bow
elif player2_weapon2 == 4:
    player2_weapon2 = shield

player2_main = Player(player2.name, player2.gender, player2.health)
player2_main.damage += player2_weapon1.damage
player2_main.defence += player2_weapon1.defence
player2_main.reach += player2_weapon1.reach

player2_secondary = Player(player2.name, player2.gender, player2.health)
player2_secondary.damage += player2_weapon2.damage
player2_secondary.defence += player2_weapon2.defence
player2_secondary.reach += player2_weapon2.reach


print("""{name}({gender}{level}), You have {health} health left. This is your statics with your main weapon: 
Damage: {damage}
Range: {reach}
Defence: {defence}

And this is your statics with your secondary weapon: 
Damage: {damage2}
Range: {reach2}
Defence: {defence2}
""".format(name=player.name, gender=player.gender, level=player.level, health=player.health, damage=player_main.damage, reach=player_main.reach, defence=player_main.defence, damage2=player_secondary.damage, reach2=player_secondary.reach, defence2=player_secondary.defence))

print("""{name}({gender}{level}), You have {health} health left. This is your statics with your main weapon: 
Damage: {damage}
Range: {reach}
Defence: {defence}

And this is your statics with your secondary weapon: 
Damage: {damage2}
Range: {reach2}
Defence: {defence2}
""".format(name=player2.name, gender=player2.gender, level=player2.level, health=player2.health, damage=player2_main.damage, reach=player2_main.reach, defence=player2_main.defence, damage2=player2_secondary.damage, reach2=player2_secondary.reach, defence2=player2_secondary.defence))

print("Here is how the game works: Each round you choose a weapon use it against your enemy, but so does the enemy. Whoever make better decisions wins, Just like how it is in life!")

check = False
while not check:
    P1ready = input("{player_name}, are you ready? Enter Y when you are ready: ".format(player_name=player_name)).upper()
    if P1ready == "Y":
        check = True
    else:
        print("Invalid input, just enter Y when you are ready.")

check = False
while not check:
    P1ready = input("{player2_name}, are you ready? Enter Y when you are ready: ".format(player2_name=player2_name)).upper()
    if P1ready == "Y":
        check = True
    else:
        print("Invalid input, just enter Y when you are ready.")

arena = [i for i in range(1, 6)]
for round in range(1, 100):
    check = False
    while not check:
        chosen_weapon1 = input("Round {round}! {player_name}, choose your weapon (Enter A for main weapon and B for secondary weapon): ".format(round=str(round), player_name=player_name)).upper()
        if chosen_weapon1 == "A" or "B":
            check = True
    check = False
    while not check:
        chosen_weapon2 = input("Round {round}! {player2_name}, choose your weapon (Enter A for main weapon and B for secondary weapon): ".format(round=str(round), player2_name=player2_name)).upper()
        if chosen_weapon2 == "A" or "B":
            check = True
        
    distance =  random.choice(arena)
    if chosen_weapon1 == "A":
        player_set = player_main
    elif chosen_weapon1 == "B":
        player_set = player_secondary
    
    if chosen_weapon2 == "A":
        player2_set = player2_main
    elif chosen_weapon2 == "B":
        player2_set = player2_secondary
    
    female_crit_chance = random.choices([True, False], weights=[40, 60], k=1)[0]

    if player_set.reach >= distance:
        if player_set.gender == "F" and female_crit_chance == True:
            player2.health = max(player2.health - max((player_set.damage - player2_set.defence) * 2, 2), 0)
            print("After {player_name}'s CRITICAL attack, {player2_name} lost {lost_health} health!".format(player_name=player_name, player2_name=player2_name, lost_health=max((player_set.damage - player2_set.defence) * 2, 2)))
        else:
            player2.health = max(player2.health - max((player_set.damage - player2_set.defence), 1), 0)
            print("After {player_name}'s attack, {player2_name} lost {lost_health} health!".format(player_name=player_name, player2_name=player2_name, lost_health=max((player_set.damage - player2_set.defence), 1)))
    elif player_set.reach < distance:
        print("{player_name}'s attack couldn't reach to {player2_name}. No damage was dealt!".format(player_name=player_name, player2_name=player2_name))

    if player2_set.reach >= distance:
        if player2_set.gender == "F" and female_crit_chance == True:
            player.health = max(player.health - max((player2_set.damage - player_set.defence) * 2, 2), 0)
            print("After {player2_name}'s CRITICAL attack, {player_name} lost {lost_health} health!".format(player2_name=player2_name, player_name=player_name, lost_health=max((player2_set.damage - player_set.defence) * 2, 2)))
        else:
            player.health = max(player.health - max((player2_set.damage - player_set.defence), 1), 0)
            print("After {player2_name}'s attack, {player_name} lost {lost_health} health!".format(player2_name=player2_name, player_name=player_name, lost_health=max((player2_set.damage - player_set.defence), 1)))
    elif player2_set.reach < distance:
        print("{player2_name}'s attack couldn't reach to {player_name}. No damage was dealt!".format(player2_name=player2_name, player_name=player_name))

    print("Remaining health:\n{player_name}: {player_health}\n{player2_name}: {player2_health}".format(player_name=player_name, player_health=max(player.health, 0), player2_name=player2_name, player2_health=max(player2.health, 0)))

    if player.health == 0 and player2.health == 0:
        print("{player_name} And {player2_name} died at the same time! The game was a tie!".format(player_name=player_name, player2_name=player2_name))
        break
    elif player.health == 0:
        print("{player_name} died! Rest in peace! {player2_name} won the game! CONGRATULATIONS!".format(player_name=player_name, player2_name=player2_name))
        break
    elif player2.health == 0:
        print("{player2_name} died! Rest in peace! {player_name} won the game! CONGRATULATIONS!".format(player_name=player_name, player2_name=player2_name))
        break
