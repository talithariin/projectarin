from tkinter import *
import random
from abc import ABCMeta, abstractmethod

### OOP: Class
class Move(object):
    ### OOP: Dictionary
    MOVES_DICTIONARY = {}
    ### OOP: Constructor
    def __init__(self, move):
        moveInfo = []
        # Only reading through the file if no information is stored in the Moves Dictionary
        if len(Move.MOVES_DICTIONARY) == 0:
            fin = open("Pokemon Moves.csv", 'r')
            for line in fin:
                line = line.strip()
                moveList = line.split(",")
                Move.MOVES_DICTIONARY[moveList[1]] = moveList  # The name of the move is the key while the rest of the
                # list is the value

            fin.close()

        # Finding the matching key in the dictionary, then assigning the list to a variable called moveInfo
        for key in Move.MOVES_DICTIONARY:
            if key.lower() == move.lower():
                moveInfo = Move.MOVES_DICTIONARY[key]

        ### OOP: Encapsulation
        # ATTRIBUTES
        # ID info
        self.moveInfo = moveInfo
        self.id = moveInfo[0]  # Move's number id
        self.name = moveInfo[1]  # Move's name

        # Description
        self.description = moveInfo[2]  # Move description
        self.type = moveInfo[3]  # Move type
        self.kind = moveInfo[4]  # Can be special, physical, or stat-changing

        # For in-battle calculations
        self.power = int(moveInfo[5])  # Move's base damage
        self.accuracy = moveInfo[6]
        self.pp = int(moveInfo[7])

    ### OOP: Abstraction (attributes & methods)
    # METHODS
    # str method
    def __str__(self):
        msg = self.name + " " + str(self.power)
        return msg

    # GET Methods
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getType(self):
        return self.type

    def getKind(self):
        return self.kind

    def getPower(self):
        return self.power

    def getAccuracy(self):
        return self.accuracy

    def getPP(self):
        return self.pp

    # SET Methods
    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setPower(self, power):
        self.power = power

    def setAccuracy(self, accuracy):
        self.accuracy = accuracy

    def setPP(self, pp):
        self.pp = pp

### OOP: Class
### OOP: Inheritance (object)
# Creating the Pokemon Class
class Pokemon(object):
    ### OOP: Dictionary
    POKEMON_DICTIONARY = {}
    # Values used to calculate Pokemon base stats
    IV = 30
    EV = 85
    STAB = 1.5  # Stands for "Same-type attack bonus"
    LEVEL = 50
    ### OOP: Constructor
    def __init__(self, pokemon):  # takes a user-selected Pokemon as an argument
        pokemonInfo = []
        if len(Pokemon.POKEMON_DICTIONARY) == 0:
            fin = open("Kanto Pokemon Spreadsheet.csv", 'r')
            for line in fin:
                line = line.strip()
                pokeList = line.split(",")
                Pokemon.POKEMON_DICTIONARY[pokeList[1]] = pokeList  # Creating key (Pokemon name) value (id info) pair

            fin.close()

        # Creating an info list for the user-selected Pokemon containing all the Pokemon attributes
        for key in Pokemon.POKEMON_DICTIONARY:
            if key.lower() == pokemon.lower():
                pokemonInfo = Pokemon.POKEMON_DICTIONARY[key]
        
        ### OOP: Encapsulation
        # ATTRIBUTES
        # Referring to the pokemonInfo list to fill in the rest of the attributes
        # ID Info
        self.__id = pokemonInfo[0]
        self.name = pokemonInfo[1]
        self.level = Pokemon.LEVEL

        # Type
        self.type1 = pokemonInfo[2]
        self.type2 = pokemonInfo[3]

        # BASE STATS
        self.__hp = int(pokemonInfo[4])
        self.__atk = int(pokemonInfo[5])
        self.__defense = int(pokemonInfo[6])
        self.__spAtk = int(pokemonInfo[7])
        self.__spDef = int(pokemonInfo[8])
        self.__speed = int(pokemonInfo[9])

        # In Battle Stats
        # The base stat is different from the in battle stat. The base stat is just used for calculating the in-battle stat
        # The in battle stats are calculated based on a formula from the games
        self.battleHP = int(self.__hp + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 60)
        self.battleATK = self.__atk + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
        self.battleDEF = self.__defense + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
        self.battleSpATK = self.__spAtk + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
        self.battleSpDEF = self.__spDef + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
        self.battleSpeed = self.__speed + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5

        # These variables are used to just hold the values of the original stat for stat modification purposes
        self.originalATK = self.__atk + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
        self.originalDEF = self.__defense + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
        self.originalSpATK = self.__spAtk + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
        self.originalSpDEF = self.__spDef + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
        self.originalSpeed = self.__speed + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5

        # Moves
        # The Kanto Pokemon Spreadsheet has pre-determined movesets
        self.move1 = Move(pokemonInfo[10])
        self.move2 = Move(pokemonInfo[11])
        self.move3 = Move(pokemonInfo[12])
        self.move4 = Move(pokemonInfo[13])

        # A list containing all the moves; used for error-checking later
        self.moveList = [self.move1.name.lower(), self.move2.name.lower(), self.move3.name.lower(), self.move4.name.lower()]

        # In Battle Stats
        # Raised or lowered based on different moves used in battle. Affects the in battle stats (more info in the Overview of Battle Mechanics in readme.txt)
        self.atkStage = 0
        self.defStage = 0
        self.spAtkStage = 0
        self.spDefStage = 0
        self.speedStage = 0

    # METHODS
    # Printing all the Pokemon info with the str method
    def __str__(self):
        msg = "Name: " + str(self.__name) + "\nID: " + str(self.__id) + "\nType1: " + str(self.__type1) + \
              "\nType2: " + str(self.__type2) + "\nBase HP: " + str(self.__hp) + "\nBase ATK: " + str(self.__atk) + "\nBase DEF: " + \
              str(self.__defense) + "\nBase Sp. ATK: " + str(self.__spAtk) + "\nBase Sp. DEF: " + str(self.__spDef) + "\nBase Speed: " + str(self.__speed)
        return msg

    ### OOP: Abstraction (attributes & methods)
    # Get Attribute METHODS
    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    # Get BASE STAT METHODS
    def getHP(self):
        return self.__hp

    def getATK(self):
        return self.__atk

    def getDEF(self):
        return self.__defense

    def getSpATK(self):
        return self.__spAtk

    def getSpDEF(self):
        return self.__spDef

    def getSpeed(self):
        return self.__speed

    # Get STAT STAGE Methods
    def getAtkStage(self):
        return self.atkStage

    def getDefStage(self):
        return self.defStage

    def getSpAtkStage(self):
        return self.spAtkStage

    def getSpDefStage(self):
        return self.spDefStage

    def getSpeedStage(self):
        return self.speed

    # Set STAT STAGE Methods
    def setAtkStage(self, atkStage):
        self.atkStage = atkStage

    def setDefStage(self, defStage):
        self.defStage = defStage

    def setSpAtkStage(self, spAtkStage):
        self.spAtkStage = spAtkStage

    def setSpDefStage(self, spDefStage):
        self.spDefStage = spDefStage

    def setSpeedStage(self, speedStage):
        self.speedStage = speedStage

    # MOVE Methods
    def getMove1(self):
        return self.move1

    def getMove2(self):
        return self.move2

    def getMove3(self):
        return self.move3

    def getMove4(self):
        return self.move4

    def setMove1(self, move1):
        self.move1 = Move(move1)

    def setMove2(self, move2):
        self.move2 = Move(move2)

    def setMove3(self, move3):
        self.move3 = Move(move3)

    def setMove4(self, move4):
        self.move4 = Move(move4)

    # Print Methods
    # These methods return strings containing information about HP and movesets
    def printHP(self):
        msg = str(self.name) + ": HP " + str(self.battleHP)
        return msg

    def printMoves(self): # Take a list of move names as argument?
        msg = "\nMove 1: " + self.move1.moveInfo[1] + "\nMove 2: " + self.move2.moveInfo[1] + "\nMove 3: " + self.move3.moveInfo[1] + "\nMove 4: " + self.move4.moveInfo[1]
        return msg

    ### OOP: Polymorphism
    # In Battle Methods
    # Takes a move as input and returns a string with the pokemon using that move
    def useMove(self, move):
        msg = self.name + " used " + move.name + "!"
        return msg

    # Takes an int as input and returns a string with the pokemon losing that much HP
    def loseHP(self, lostHP):
        self.battleHP -= lostHP
        # Making sure battlHP doesn't fall below 0
        if self.battleHP <= 0:
            self.battleHP = 0
        msg = self.name + " lost " + str(lostHP) + " HP!"
        return msg

    # Takes an int as input and returns a string with the pokemon gaining that much HP
    def gainHP(self, gainedHP):
        self.__hp += gainedHP

    # Determines if the Pokemon still has HP and returns a boolean
    def isAlive(self):
        if self.battleHP > 0:
            return True
        else:
            return False

    # If battleHP is 0, returns a string showing that the Pokemon fainted
    def faint(self):
        if self.battleHP <= 0:
            msg = self.name + " fainted "
            return msg

# Stat modification function; will be called inside the attack function if the move alters the defending Pokemon's stats
# Takes the current statStage as input and returns a multiplier that will be used to calculate the new statStage
def statMod(statStage):
    if statStage == 1:
        multiplier = 1.5
    elif statStage == -1:
        multiplier = 2/3
    elif statStage == 2:
        multiplier = 2
    elif statStage == -2:
        multiplier = 1/2
    elif statStage == 3:
        multiplier = 2.5
    elif statStage == -3:
        multiplier = 0.4
    elif statStage == 4:
        multiplier = 3
    elif statStage == -4:
        multiplier = 1/3
    elif statStage == 5:
        multiplier = 3.5
    elif statStage == -5:
        multiplier = 2/7
    elif statStage == 6:
        multiplier = 4
    elif statStage == -6:
        multiplier = 1/4

    return multiplier  # This multiplier affects the value of the in-battle stat

### OOP: Instance 
# Will take a move, the attacking Pokemon object, and the defending Pokemon object as input
# Will return a string that contains the amount of damage done and the effectiveness of the move
def attack(move, pokemon1, pokemon2):
    # Creating an empty string to store the results of the attack function
    tempMsg= ""

    # Reading "Type Advantages.csv" file to determine type advantages and the damage modifier
    # Stores the line number in the csv as the key and a list giving information about type advantage for the value
    fin = open("Type Advantages.csv", 'r')
    typeDic = {}
    for line in fin:
        line = line.strip()
        typeList = line.split(",")
        typeDic[typeList[0]] = typeList
        # This list contains a number in the first position, the attack type in the second, the defending type in the third,
        # and the appropriate damage multiplier in the fourth
    fin.close()

    # Making the input string into an actual move object
    move = Move(move)

    # This modifier is used in damage calculations; it takes into account type advantage and STAB bonus
    modifier = 1

    # Calculating Type advantages using "Type Advantages.csv" file
    for key in typeDic:
        # If the attacking and defending types match up, multiply the modifier by the damage multiplier from the list
        if typeDic[key][1] == move.type and typeDic[key][2] == pokemon2.type1:
            modifier *= float(typeDic[key][3])

        # Didn't use elif; Just in case you get a 4x or 0.25x modifier based on double type
        if typeDic[key][1] == move.type and typeDic[key][2] == pokemon2.type2:
            modifier *= float(typeDic[key][3])

    ### OOP: Encapsulation
    # Calculating STAB (Same-type Attack Bonus)
    if move.type == pokemon1.type1:
        modifier *= Pokemon.STAB

    elif move.type == pokemon1.type2:
        modifier *= Pokemon.STAB

    # Damage formula also has a random element
    modifier *= random.uniform(0.85, 1.0)

    print()

    ### OOP: Polymorphism
    # Appending the useMove function to the output
    tempMsg += pokemon1.useMove(move)

    ### OOP: Abstraction
    # ATK/DEF or SpATK/SpDEF or Status? Using the Pokemon damage formula
    # If the move is "Physical", the damage formula will take into account attack and defense
    if move.kind == "Physical":
        damage = int((((2*pokemon1.getLevel()) + 10)/250 * (pokemon1.battleATK/pokemon2.battleDEF) * move.getPower() + 2) * modifier)
        tempMsg += "\n" + pokemon2.loseHP(damage)
    # If the move is "Special", the damage formula will take into account special attack and special defense
    elif move.kind == "Special":
        damage = int((((2*pokemon1.getLevel()) + 10)/250 * (pokemon1.battleSpATK/pokemon2.battleSpDEF) * move.getPower() + 2) * modifier)
        tempMsg += "\n" + pokemon2.loseHP(damage)


    # Stat Changing moves
    else:
        # If the move is stat-changing, it does 0 damage and the modifier is set to 1 (so it doesn't return super effective or not very effective)
        damage = 0
        modifier = 1

        # Going through each kind of different stat change based on the move type
        if move.kind == "a-":
            pokemon2.atkStage -= 1
            pokemon2.battleATK = pokemon2.originalATK * statMod(pokemon2.atkStage)
            tempMsg += "\n" + pokemon2.name + "'s attack fell! "

        elif move.kind == "a+":
            pokemon1.atkStage +=1
            pokemon1.battleATK = pokemon1.originalATK * statMod(pokemon1.atkStage)
            tempMsg += "\n" + pokemon1.name + "'s attack rose! "

        elif move.kind == "d+":
            pokemon1.defStage +=1
            pokemon1.battleDEF = pokemon1.originalDEF * statMod(pokemon1.defStage)
            print(pokemon1.name + "'s defense rose! ")
            tempMsg += "\n" + pokemon1.name + "'s defense rose! "

        elif move.kind == "sa+":
            pokemon1.spAtkStage +=1
            pokemon1.battleSpATK = pokemon1.originalSpATK * statMod(pokemon1.spAtkStage)
            print(pokemon1.name + "'s special attack rose! ")
            tempMsg += "\n" + pokemon1.name + "'s special attack rose! "

        elif move.kind == "sd+":
            pokemon1.spDefStage +=1
            pokemon1.battleSpDef = pokemon1.originalSpDEF * statMod(pokemon1.spDefStage)
            tempMsg += "\n" + pokemon1.name + "'s special defense rose! "

        elif move.kind == "s+":
            pokemon1.speedStage +=1
            pokemon1.battleSpeed = pokemon1.originalSpeed * statMod(pokemon1.speedStage)
            tempMsg += "\n" + pokemon1.name + "'s speed fell! "

        elif move.kind == "d-":
            pokemon2.defStage -=1
            pokemon2.battleDEF = pokemon2.originalDEF * statMod(pokemon2.defStage)
            tempMsg += "\n" + pokemon2.name + "'s defense fell! "

        elif move.kind == "sa-":
            pokemon2.spAtkStage -=1
            pokemon2.battleSpATK = pokemon2.originalSpATK * statMod(pokemon2.spAtkStage)
            tempMsg += "\n" + pokemon2.name + "'s special attack fell! "

        elif move.kind == "sd-":
            pokemon2.spDefStage -=1
            pokemon2.battleSpDEF = pokemon2.originalSpDEF * statMod(pokemon2.spDefStage)
            tempMsg += "\n" + pokemon2.name + "'s special defense fell! "

        elif move.kind == "s-":
            pokemon2.speedStage -=1
            pokemon2.battleSpeed = pokemon2.originalSpeed * statMod(pokemon2.speedStage)
            tempMsg += "\n" + pokemon2.name + "'s speed fell! "

    # Super effective, not very effective, or no effect?
    # Appending the result to tempMsg
    if modifier < 0.85 and modifier > 0:
        tempMsg += "\nIt's not very effective..."

    elif modifier > 1.5:
        tempMsg += "\nIt's super effective!"

    elif modifier == 0.0:
        tempMsg += "\nIt doesn't affect " + pokemon2.name + "..."

    # String containing useMove(), damage, and type effectiveness
    return tempMsg

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        # Assigning string variables for user text entry
        self.userStrVar = StringVar()
        self.userStrVar.set("")

        self.cpuStrVar = StringVar()
        self.cpuStrVar.set("")

        self.moveStrVar1 = StringVar()
        self.moveStrVar1.set("")

        self.moveStrVar2 = StringVar()
        self.moveStrVar2.set("")

        # WIDGETS
        # Buttons
        self.pokedexBtn = Button(self, text="See All Pokemon", command=self.seePokedex)
        self.pokedexBtn.grid(row=0, column=1)

        self.checkBtn = Button(self, text="Lock In", command=self.checkPokemon)
        self.checkBtn.grid(row=1, column=1)

        self.battleBtn = Button(self, text="Begin Battle", state=DISABLED, command=self.beginBattle)
        self.battleBtn.grid(row=2, column=1)

        self.moveBtn1 = Button(self, text="Select Move", state=DISABLED, command=self.selectMove1)
        self.moveBtn1.grid(row=7, column=0)

        self.moveBtn2 = Button(self, text="Select Move", state=DISABLED, command=self.selectMove2)
        self.moveBtn2.grid(row=7, column=2)

        self.restartBtn = Button(self, text="Restart?", state=DISABLED, command=self.restart)
        self.restartBtn.grid(row=7, column=1)

        # Labels, Entry fields, and Text Boxes
        self.entLabel1 = Label(self, text="Choose your Pokemon: ")
        self.entLabel1.grid(row=0, column=0)

        self.entName1 = Entry(self, textvariable=self.userStrVar)  # Pokemon name entry
        self.entName1.grid(row=1, column=0, rowspan=2)

        self.moveText1 = Text(self, width=20, height=8, state=DISABLED)  # Text box with moveset and HP
        self.moveText1.grid(row=5, column=0, sticky=S)

        self.entLabel2 = Label(self, text="Choose your opponent: ")
        self.entLabel2.grid(row=0, column=2)

        self.entName2 = Entry(self, textvariable=self.cpuStrVar)  # Pokemon name entry
        self.entName2.grid(row=1, column=2, rowspan=2)

        self.moveText2 = Text(self, width=20, height=8, state=DISABLED)  # Text box with moveset and HP
        self.moveText2.grid(row=5, column=2, sticky=S)

        self.txtStats = Text(self, width=50, height=10, state=DISABLED)  # Main text box
        self.txtStats.grid(row=3, column=1)

        self.moveEnt1 = Entry(self, textvariable=self.moveStrVar1, state=DISABLED)  # Move entry field 1
        self.moveEnt1.grid(row=6,column=0)

        self.moveEnt2 = Entry(self, textvariable=self.moveStrVar2, state=DISABLED)  # Move entry field 2
        self.moveEnt2.grid(row=6, column=2)

        # Sprites
        tempImg = PhotoImage(file="Sprites/white.gif")  # first putting a blank image for each sprite, will replace later after pressing "Begin Battle"

        # Creating an image label object for each sprite
        self.sprite1Label = Label(self, image=tempImg)
        self.sprite1Label.image = tempImg
        self.sprite1Label.grid(row=3, column=0)

        self.sprite2Label = Label(self, image=tempImg)
        self.sprite2Label.image = tempImg
        self.sprite2Label.grid(row=3, column=2)


        # Pokemon Objects
        # Blank until the user enters which Pokemon they want
        self.userPokemon = None
        self.cpuPokemon = None

    # Creating a method to print the list of all Pokemon
    def seePokedex(self):
        self.txtStats.config(state=NORMAL)
        self.txtStats.delete(0.0, END)
        for pokemon in pokedex:
            self.txtStats.insert(END, "\n" + pokemon)
        self.txtStats.config(state=DISABLED)

    # Creating a method to check if the Pokemon are valid and actually usable
    # Returns an error message if the Pokemon are not usable
    def checkPokemon(self):
        if self.userStrVar != "" and self.cpuStrVar != "":
            if self.userStrVar.get().lower() in pokedex and self.cpuStrVar.get().lower() in pokedex:
                self.txtStats.config(state=NORMAL)
                self.txtStats.delete(0.0, END)
                self.txtStats.insert(0.0, "You are ready to battle.")
                self.txtStats.config(state=DISABLED)

                self.checkBtn.config(state=DISABLED)
                self.entName1.config(state=DISABLED)
                self.entName2.config(state=DISABLED)
                self.pokedexBtn.config(state=DISABLED)
                self.battleBtn.config(state=NORMAL)

                self.userPokemon = Pokemon(self.userStrVar.get())
                self.cpuPokemon = Pokemon(self.cpuStrVar.get())

            # Returning an error message if Pokemon are not valid
            else:
                self.txtStats.config(state=NORMAL)
                self.txtStats.delete(0.0, END)
                self.txtStats.insert(0.0, "Please make sure the Pokemon you've entered are in the Pokedex")
                self.txtStats.config(state=DISABLED)
                self.battleBtn.config(state=DISABLED)

    # Creating a method to actually start the battle
    def beginBattle(self):
        # Replacing the blank image with the actual sprites of the appropriate Pokemon
        # Using the user-input string to determine which sprite image to use
        self.sprite1 = PhotoImage(file="Sprites/" + self.userStrVar.get().lower() + ".gif")
        self.sprite1Label.configure(image=self.sprite1)
        self.sprite1Label.image = self.sprite1

        self.sprite2 = PhotoImage(file="Sprites/" + self.cpuStrVar.get().lower() + ".gif")
        self.sprite2Label.configure(image=self.sprite2)
        self.sprite2Label.image = self.sprite2

        # Printing each Pokemon's HP and moveset to its respective box
        self.moveText1.config(state=NORMAL)
        self.moveText2.config(state=NORMAL)
        self.moveText1.delete(0.0, END)
        self.moveText2.delete(0.0, END)
        self.moveText1.insert(0.0, self.userPokemon.printHP() + "\n" + self.userPokemon.printMoves())
        self.moveText2.insert(0.0, self.cpuPokemon.printHP() + "\n" + self.cpuPokemon.printMoves())
        self.moveText1.config(state=DISABLED)
        self.moveText2.config(state=DISABLED)

        # Deciding which Pokemon to enable first based on the speed (battleSpeed) stat
        if self.userPokemon.isAlive() and self.cpuPokemon.isAlive():
            if self.userPokemon.battleSpeed >= self.cpuPokemon.battleSpeed:
                self.moveEnt1.config(state=NORMAL)
                self.moveBtn1.config(state=NORMAL)
            elif self.cpuPokemon.battleSpeed > self.userPokemon.battleSpeed:
                self.moveEnt2.config(state=NORMAL)
                self.moveBtn2.config(state=NORMAL)
        self.battleBtn.config(state=DISABLED)

    # Method takes the user-inputted string and plugs it into the attack function
    # Prints the result of the attack function to the center text box
    def selectMove1(self):
        if self.moveStrVar1.get().lower() in self.userPokemon.moveList:
            self.txtStats.config(state=NORMAL)
            self.txtStats.delete(0.0, END)
            self.txtStats.insert(0.0, attack(self.moveStrVar1.get(), self.userPokemon, self.cpuPokemon))
            self.txtStats.config(state=DISABLED)

            # Updating the info for both Pokemon after the move has been used
            self.moveText1.config(state=NORMAL)
            self.moveText2.config(state=NORMAL)
            self.moveText1.delete(0.0, END)
            self.moveText2.delete(0.0, END)
            self.moveText1.insert(0.0, self.userPokemon.printHP() + "\n" + self.userPokemon.printMoves())
            self.moveText2.insert(0.0, self.cpuPokemon.printHP() + "\n" + self.cpuPokemon.printMoves())
            self.moveText1.config(state=DISABLED)
            self.moveText2.config(state=DISABLED)

            # If one of the Pokemon faints, this method will end the battle by disabling all other buttons/fields except
            # for the Restart button
            if not self.cpuPokemon.isAlive():
                self.txtStats.config(state=NORMAL)
                self.txtStats.insert(END, "\n" + self.cpuPokemon.faint())
                self.txtStats.insert(END, "\nPlay again?")
                self.txtStats.config(state=DISABLED)
                self.moveEnt1.delete(0, END)
                self.restartBtn.config(state=NORMAL)
                self.moveBtn1.config(state=DISABLED)
                self.moveEnt1.config(state=DISABLED)
                self.battleBtn.config(state=DISABLED)

            # If both Pokemon are alive, this method will disable the current Pokemon and enable the opposing Pokemon so
            # it can make its move as well
            else:
                self.moveEnt1.delete(0, END)
                self.moveEnt1.config(state=DISABLED)
                self.moveBtn1.config(state=DISABLED)
                self.moveEnt2.config(state=NORMAL)
                self.moveBtn2.config(state=NORMAL)

    # Does the same thing as selectMove1() just with respect to the other Pokemon
    def selectMove2(self):
        if self.moveStrVar2.get().lower() in self.cpuPokemon.moveList:
            self.txtStats.config(state=NORMAL)
            self.txtStats.delete(0.0, END)
            self.txtStats.insert(0.0, attack(self.moveStrVar2.get(), self.cpuPokemon, self.userPokemon))
            self.txtStats.config(state=DISABLED)

            # Updating the info for the other Pokemon
            self.moveText1.config(state=NORMAL)
            self.moveText2.config(state=NORMAL)
            self.moveText1.delete(0.0, END)
            self.moveText2.delete(0.0, END)
            self.moveText1.insert(0.0, self.userPokemon.printHP() + "\n" + self.userPokemon.printMoves())
            self.moveText2.insert(0.0, self.cpuPokemon.printHP() + "\n" + self.cpuPokemon.printMoves())
            self.moveText1.config(state=DISABLED)
            self.moveText2.config(state=DISABLED)

            if not self.userPokemon.isAlive():
                self.txtStats.config(state=NORMAL)
                self.txtStats.insert(END, "\n" + self.userPokemon.faint())
                self.txtStats.insert(END, "\nPlay again?")
                self.txtStats.config(state=DISABLED)
                self.moveEnt2.delete(0, END)
                self.restartBtn.config(state=NORMAL)
                self.moveText1.config(state=DISABLED)
                self.moveText2.config(state=DISABLED)
                self.moveEnt2.config(state=DISABLED)
                self.moveBtn2.config(state=DISABLED)
                self.battleBtn.config(state=DISABLED)

            else:
                self.moveEnt2.delete(0, END)
                self.moveEnt2.config(state=DISABLED)
                self.moveBtn2.config(state=DISABLED)
                self.moveEnt1.config(state=NORMAL)
                self.moveBtn1.config(state=NORMAL)

    # Completely clears and resets all text fields, buttons, and images to their original state
    def restart(self):
        # Resetting the Pokemon objects
        self.userPokemon = None
        self.cpuPokemon = None

        # Resetting all the widgets
        self.txtStats.config(state=NORMAL)
        self.moveText1.config(state=NORMAL)
        self.moveText2.config(state=NORMAL)

        self.txtStats.delete(0.0, END)
        self.moveText1.delete(0.0, END)
        self.moveText2.delete(0.0, END)
        self.moveEnt1.delete(0, END)
        self.moveEnt2.delete(0, END)

        self.txtStats.config(state=DISABLED)
        self.moveText1.config(state=DISABLED)
        self.moveText2.config(state=DISABLED)

        # Enabling widgets so the window returns to its original state
        self.entName1.config(state=NORMAL)
        self.entName1.delete(0, END)

        self.entName2.config(state=NORMAL)
        self.entName2.delete(0, END)

        self.checkBtn.config(state=NORMAL)
        self.pokedexBtn.config(state=NORMAL)

        # Disabling the restart button so the user can't constantly restart the game
        self.restartBtn.config(state=DISABLED)

        # Resetting the Sprites
        tempImg = PhotoImage(file="Sprites/white.gif")
        self.sprite1Label.configure(image=tempImg)
        self.sprite1Label.image = tempImg

        self.sprite2Label.configure(image=tempImg)
        self.sprite2Label.image = tempImg

# Global variables and initialization
pokedex = []

# Function to read the Pokemon spreadsheet and populate the pokedex list
def read_pokedex():
    global pokedex
    fin = open("Kanto Pokemon Spreadsheet.csv", 'r')
    pokemonDictionary = {}

    for line in fin:
        line = line.strip()
        pokeList = line.split(",")
        pokemonDictionary[pokeList[1]] = pokeList

    fin.close()

    for key in pokemonDictionary:
        pokedex.append(pokemonDictionary[key][1].lower())
        pokedex.sort()

# Function to check Pokemon validity
def check_pokemon(user_str, cpu_str):
    if self.userStrVar != "" and self.cpuStrVar != "":
        if self.userStrVar.get().lower() in pokedex and self.cpuStrVar.get().lower() in pokedex:
            self.txtStats.config(state=NORMAL)
            self.txtStats.delete(0.0, END)
            self.txtStats.insert(0.0, "You are ready to battle.")
            self.txtStats.config(state=DISABLED)

            self.checkBtn.config(state=DISABLED)
            self.entName1.config(state=DISABLED)
            self.entName2.config(state=DISABLED)
            self.pokedexBtn.config(state=DISABLED)
            self.battleBtn.config(state=NORMAL)

            self.userPokemon = Pokemon(self.userStrVar.get())
            self.cpuPokemon = Pokemon(self.cpuStrVar.get())

        # Returning an error message if Pokemon are not valid
        else:
            self.txtStats.config(state=NORMAL)
            self.txtStats.delete(0.0, END)
            self.txtStats.insert(0.0, "Please make sure the Pokemon you've entered are in the Pokedex")
            self.txtStats.config(state=DISABLED)
            self.battleBtn.config(state=DISABLED)

def beginBattle(user_pokemon, cpu_pokemon):
        # Replacing the blank image with the actual sprites of the appropriate Pokemon
        # Using the user-input string to determine which sprite image to use
        self.sprite1 = PhotoImage(file="Sprites/" + self.userStrVar.get().lower() + ".gif")
        self.sprite1Label.configure(image=self.sprite1)
        self.sprite1Label.image = self.sprite1

        self.sprite2 = PhotoImage(file="Sprites/" + self.cpuStrVar.get().lower() + ".gif")
        self.sprite2Label.configure(image=self.sprite2)
        self.sprite2Label.image = self.sprite2

        # Printing each Pokemon's HP and moveset to its respective box
        self.moveText1.config(state=NORMAL)
        self.moveText2.config(state=NORMAL)
        self.moveText1.delete(0.0, END)
        self.moveText2.delete(0.0, END)
        self.moveText1.insert(0.0, self.userPokemon.printHP() + "\n" + self.userPokemon.printMoves())
        self.moveText2.insert(0.0, self.cpuPokemon.printHP() + "\n" + self.cpuPokemon.printMoves())
        self.moveText1.config(state=DISABLED)
        self.moveText2.config(state=DISABLED)

        # Deciding which Pokemon to enable first based on the speed (battleSpeed) stat
        if self.userPokemon.isAlive() and self.cpuPokemon.isAlive():
            if self.userPokemon.battleSpeed >= self.cpuPokemon.battleSpeed:
                self.moveEnt1.config(state=NORMAL)
                self.moveBtn1.config(state=NORMAL)
            elif self.cpuPokemon.battleSpeed > self.userPokemon.battleSpeed:
                self.moveEnt2.config(state=NORMAL)
                self.moveBtn2.config(state=NORMAL)
        self.battleBtn.config(state=DISABLED)

# Main function
def main():
    root = Tk()
    root.title("Pokemon Battle")
    root.geometry("670x500")

    read_pokedex()

    app = Application(root)
    app.mainloop()

if __name__ == "__main__":
    main()
