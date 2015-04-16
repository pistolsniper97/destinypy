class character():
    def __init__(self):
        self.name = ""
        self.race = ""
        self.job = ""
        self.subjob = ""
        self.destination = ""
        self.currentmap = ""


class player(character):
    def __init__(self):
        character.__init__(self)
        self.status = ""
        self.health = 1
        self.defense = 1
        self.light = 1
        self.level = 1
        self.explevel = 1
        self.experience = 1
        if self.experience >= 1000 & self.explevel:
            self.explevel += 1
            self.experience -= 1000
        self.attack = 1
        self.glimmer = 1
        self.vanguardmarks = 1
        self.commendations = 1
        self.made = 0
        self.primaryw = ""
        self.armor = ""

    def status(self):
        if self.made == 1:
            print("Name: %s" % self.name)
            print("Race: %s" % self.race)
            print("Class: %s" % self.job)
            print("Subclass: %s" % self.subjob)
            print("Level: %s" % self.level)
            print("Primary: %s" % self.primaryw)
        else:
            print("Please make a character.")

    def createcharacter(self):
        if self.made == 0:
            self.name = input("Character Name: ")
            self.race = input("Choose a Race 'Human', 'Awoken', or 'Exo': ")
            self.job = input("Choose a Class 'Titan', 'Hunter', or 'Warlock': ")
            if self.job == "Titan":
                self.subjob = input("Choose a Subclass 'Defender' or 'Striker': ")
            elif self.job == "Warlock":
                self.subjob = input("Choose a Subclass 'Sunsinger' or 'Voidwalker': ")
            elif self.job == "Hunter":
                self.subjob = input("Choose a Subclass 'Gunslinger' or 'Bladedancer': ")
            self.made += 1
            del Cmd['create character']
        else:
            print("You already have a character.")

    def help(self):
        print(Cmd.keys())

    def orbit(self):
        if self.made == 1:
            if self.destination != "Space":
                print("Do you want to return to orbit?")
                goorbit = input("'yes' or 'no': ")
                if goorbit == "yes":
                    print("Your ship gracefully swoops down and picks you up.")
                    self.destination = "Space"
                    if Cmd.keys() == 'shop':
                            del Cmd['shop']
            else:
                print("You are already in orbit")
        else:
            print("Make a character first.")

    def travel(self):
        if self.made == 1:
            if self.destination == "Space":
                answer = input("Where would you like to go? \n %s: " % planets)
                if answer == "earth":
                    self.destination = "Earth"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Earth")
                elif answer == "tower":
                    self.destination = "Tower"
                    self.currentmap = ""
                    Cmd['shop'] = player.shop
                    print("Initiating Warp Drive")
                    print("Welcome to the Tower")
                elif answer == "moon":
                    self.destination = "Moon"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to the Moon")
                elif answer == "venus":
                    self.destination = "Venus"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Venus")
                elif answer == "mars":
                    self.destination = "Mars"
                    self.currentmap = ""
                    print("Initiating Warp Drive")
                    print("Welcome to Mars")
                else:
                    print(invalidinput)
        else:
            print("Make a character first.")
            
    def inventory(self):
        print(inventory2)
        print("%s glimmer" % self.glimmer)
        print("%s vanguard marks" % self.vanguardmarks)

    def equip(self):
        if self.made != 1:
            print("Create a character first.")
        else:
            print("What would you like to equip?")
            liste = input("Weapon or Armor: ")
            if liste == "Weapon":
                print("Choose a weapon from below")
                print(weaponinv)
                equipweapon = input("Select One: ")
                if self.primaryw == "":
                    self.primaryw = equipweapon
                    weaponinv.remove(equipweapon)
                else:
                    weaponinv.append(self.primaryw)
                    self.primaryw = equipweapon
                    weaponinv.remove(equipweapon)
            if liste == "Armor":
                print("Choose which armor you want to equip")
                print(armorinv)
                equiparmor = input("Select one: ")
                if self.armor == "":
                    self.armor = equiparmor
                    armorinv.remove(equiparmor)
                else:
                    armorinv.append(self.armor)
                    self.armor = equiparmor
                    armorinv.remove(equiparmor)

    def explore(self):
        if self.made == 0:
            print("Make a character first.")
        else:
            if self.destination == "Tower":
                print("Looks like there are some shops to visit")
            elif self.destination == "Earth":
                print("Lets explore Earth!")
            else:
                print("travel to another destination.")

    def shop(self):
        if self.glimmer >= 0:
            print("What would you like?")
            shopping = input("weapons or armor: ")
            if shopping == "weapons":
                print(weaponshop)
                purchase1 = input("Please choose a weapon: ")
                if self.glimmer >= weaponshop[purchase1]:
                    self.glimmer -= weaponshop[purchase1]
                    weaponinv.append(purchase1)
                    print("Thank you for shopping")
                else:
                    print("You do not have enough glimmer for %s" % purchase1)
            elif shopping == "armor":
                print(armorshop)
                purchase = input("Please choose a armor set: ")
                if self.glimmer >= armorshop[purchase]:
                    self.glimmer -= armorshop[purchase]
                    armorinv.append(purchase)
                else:
                    print("You do not have enough glimmer for %s" % purchase)
        else:
            print("You should gather more glimmer")

    def giveglimmer(self):
        print("How much glimmer do you want? ")
        glimmer2 = input()
        self.glimmer += int(glimmer2)
        print("%s glimmer has been added to your account" % glimmer2)

    def view(self):
        if self.destination == "Tower":
            print("You look at the view from the Tower.")

invalidinput = print("Invalid input")

race = {"human", "awoken", "exo", }

job = {"titan", "hunter", "warlock", }

inventory2 = []

weaponinv = ["Starter Hand Cannon", ]

armorinv = ["Starter Set", ]

planets = ["tower", "earth", "moon", "venus", "mars", ]

weaponshop = {'Hawkmoon': 2000, }

armorshop = {'VoG set': 4000, }

p = player()

print("Welcome to Destiny")
print("Connecting to Destiny servers...")
print("Connection Successful")
print("Type: help \n for a list of commands")

Cmd = {
    "status": player.status,
    "create character": player.createcharacter,
    "help": player.help,
    "travel": player.travel,
    "inventory": player.inventory,
    "equip": player.equip,
    "explore": player.explore,
    "give glimmer": player.giveglimmer,
    "go to orbit": player.orbit,
    }


while p.health > 0:
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Cmd.keys():
            if args[0] == c[:len(args[0])]:
                Cmd[c](p)
                commandFound = True
                break
        if not commandFound:
            print("%s doesn't understand the suggestion." % p.name)