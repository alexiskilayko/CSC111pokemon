# ------------------------------------------------------
#        Name: Alexis Kilayko (I did not collaborate
#              with anyone on this assignment)
#    Filename: pokemon.py
#        Date: 13 November 2018
# Description: This is a Python program that creates a simplified
#              Pokemon game.
# ------------------------------------------------------

import random

# DEFINING POKEMON CLASS

class Pokemon:

    # default attributes of pokemon
    def __init__ (self):
        
        self.name = "NAME"
        self.poketype = "NORMAL"
        self.max_hp = random.randint(25, 50)
        self.current_hp = self.max_hp # current hp starts at max hp
        self.attack_power = random.randint(20, self.max_hp)
        self.defensive_power = random.randint(20, self.max_hp)
        self.strength = [] # empty list of types pokemon is strong against
        self.weakness = [] # empty list of types pokemon is weak against
        self.moves = [] # empty list of moves
        self.fainted = False # start out not fainted
        self.revives = 2 # start out with 2 revives

    # function to print out stats of pokemon
    def printStats(self):
        
        print("-"*20) # border
        print("")
        print(self.name.upper())
        print("Type:", self.poketype.title()) 
        print("Max HP:", self.max_hp)
        print("Current HP:", self.current_hp)
        print("Attack:", self.attack_power)
        print("Defense:", self.defensive_power)
        print("")
        print("-"*20) # border
        print("")

    # "defend" function defined in advance for use in attack function
    def defend(self):

        self.current_hp = self.current_hp - ((self.defensive_power)//4)
    
        if self.current_hp <= 0:
            self.current_hp = 0
            self.fainted = True

    # attack function
    def attack(self, opponent):

        # prints pkmn's moves numbered 1 to 3
        print(self.name + "'s moves are (1)", self.moves[0], "(2)", self.moves[1], "(3)", self.moves[2] + ".")
        print("")
        choice = eval(input("What will you do? (select number): "))-1 # ask user which move to use
        print("")

        print(">>", self.name, "used", self.moves[choice] + ".") # move select message
        print("")
              
        if choice == 0: # move is same type as pokemon
        
            if opponent.poketype in self.strength: # attacking pkmn's type is strong against defending pkmn's type

                # execute defend function four times
                opponent.defend()
                opponent.defend()
                opponent.defend()
                opponent.defend()
                print(">> It's super effective!") # super effective message
                print("")

            elif opponent.poketype in self.weakness: # attacking pkmn's type is weak against defending pkmn's type 

                opponent.defend() # execute defend function once
                print(">> It's not very effective...") # not effective message
                print("")

            else: # attacking pkmn's type is neither strong nor weak against defending pkmn's type

                # execute defend function twice
                opponent.defend()
                opponent.defend()

        elif choice == 1: # move is normal type

            # normal neither effective nor weak against any pokemon in list so execute defend function twice
            opponent.defend()
            opponent.defend()

        elif choice == 2: # move changes stats

            opponent.defensive_power = int(opponent.defensive_power/1.05) # lower opponent's defense
            print(">>", opponent.name + "'s defense was lowered!") # defense lowered message
            print("")

    # function for reviving pokemon
    def revive(self, opponent):

        # used when self.fainted = True and therefore self.current_hp = 0
        self.current_hp = self.max_hp//2 # raise hp from 0 to half of max hp
        self.fainted = False # reset pokemon to not fainted
        print(">>", self.name, "has been revived!") # revived message
        print("")
        self.printStats() # print pokemon stats


# DEFINING POKEMON SUBCLASSES

class Pikachu(Pokemon):

    def __init__ (self): # redefine attributes specific to pikachu
        
        self.name = "PIKACHU"
        self.poketype = "ELECTRIC"
        self.max_hp = random.randint(25, 50)
        self.current_hp = self.max_hp
        self.attack_power = random.randint(20, self.max_hp)
        self.defensive_power = random.randint(20, self.max_hp)
        self.strength = ["FLYING", "WATER"]
        self.weakness = ["GRASS", "ELECTRIC"]
        self.moves = ["Thunder Shock", "Quick Attack", "Tail Whip"]
        self.fainted = False
        self.revives = 2

class Bulbasaur(Pokemon):

    def __init__ (self): # redefine attributes specific to bulbasaur
        
        self.name = "BULBASAUR"
        self.poketype = "GRASS"
        self.max_hp = random.randint(25, 50)
        self.current_hp = self.max_hp
        self.attack_power = random.randint(20, self.max_hp)
        self.defensive_power = random.randint(20, self.max_hp)
        self.strength = ["WATER"]
        self.weakness = ["FIRE", "FLYING"]
        self.moves = ["Vine Whip", "Tackle", "Tail Whip"]
        self.fainted = False
        self.revives = 2

class Charmander(Pokemon):

    def __init__ (self): # redefine attributes specific to charmander
        
        self.name = "CHARMANDER"
        self.poketype = "FIRE"
        self.max_hp = random.randint(25, 50)
        self.current_hp = self.max_hp
        self.attack_power = random.randint(20, self.max_hp)
        self.defensive_power = random.randint(20, self.max_hp)
        self.strength = ["GRASS"]
        self.weakness = ["FIRE", "WATER"]
        self.moves = ["Ember", "Scratch", "Tail Whip"]
        self.fainted = False
        self.revives = 2

class Squirtle(Pokemon):

    def __init__ (self): # redefine attributes specific to squirtle
        
        self.name = "SQUIRTLE"
        self.poketype = "WATER"
        self.max_hp = random.randint(25, 50)
        self.current_hp = self.max_hp
        self.attack_power = random.randint(20, self.max_hp)
        self.defensive_power = random.randint(20, self.max_hp)
        self.strength = ["FIRE"]
        self.weakness = ["WATER", "GRASS"]
        self.moves = ["Water Gun", "Tackle", "Tail Whip"]
        self.fainted = False
        self.revives = 2

class Pidgey(Pokemon): # redefine attributes specific to pidgey

    def __init__ (self):
        
        self.name = "PIDGEY"
        self.poketype = "FLYING"
        self.max_hp = random.randint(25, 50)
        self.current_hp = self.max_hp
        self.attack_power = random.randint(20, self.max_hp)
        self.defensive_power = random.randint(20, self.max_hp)
        self.strength = ["GRASS"]
        self.weakness = ["ELECTRIC"]
        self.moves = ["Gust", "Quick Attack", "Tail Whip"]
        self.fainted = False
        self.revives = 2


# DEFINING GAME SETUP

def setup():

    # title screen
    print("""
             _                              
            | |                             
 _ __   ___ | | _____ _ __ ___   ___  _ __  
| '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
| |_) | (_) |   <  __/ | | | | | (_) | | | |
| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
| |                                         
|_|
""")
    
    # pokemon select
    print("""You and your friend happen upon a box of Pokemon.
You decide to battle!  Which Pokemon will you choose?

1) PIKACHU
2) BULBASAUR
3) CHARMANDER
4) SQUIRTLE
5) PIDGEY
""")

    # setting subclasses to variables
    pika = Pikachu()
    bulb = Bulbasaur()
    char = Charmander()
    squirt = Squirtle()
    pidge = Pidgey()

    # defining list of variables of subclasses
    pokelist = [pika, bulb, char, squirt, pidge]

    # ask user which number pokemon they want to use
    player1 = eval(input("PLAYER 1 sends out... (select number): "))-1    
    player2 = eval(input("PLAYER 2 sends out... (select number): "))-1
    print("")

    # user choice becomes index of pokelist, set these list indexes to variables
    pokemon1 = pokelist[player1]
    pokemon2 = pokelist[player2]

    # print starting stats of both pokemon
    pokemon1.printStats()
    print("VS.")
    print("")
    pokemon2.printStats()

    # list of 2 selected pokemon
    playingpokemon = [pokemon1, pokemon2]

    # returning the list of 2 selected pokemon to be taken as argument of battle function
    return playingpokemon


# DEFINING WINNING SCREEN

def win():
    
    print("""
 _____                             _         _       _   _                 _ 
/  __ \                           | |       | |     | | (_)               | |
| /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___| |
| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
| \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
 \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                    __/ |                                                    
                   |___/
""")


# DEFINING BATTLE FUNCTION

def battle(playingpokemon):

    # defining variables for 2 pokemon in list
    pokemon1 = playingpokemon[0]
    pokemon2 = playingpokemon[1]

    # set arbitrary variable gameplaying as True for game to play continuously
    gameplaying = True

    # loop for while gameplaying is True, game ends when gameplaying is False
    while gameplaying == True:

        # both pkmn alive
        if pokemon1.fainted == False and pokemon2.fainted == False:

            print("It is", pokemon1.name + "'s turn.") # turn message
            pokemon1.attack(pokemon2) # pkmn 1 attacks pkmn 2
            pokemon2.printStats() # pkmn 2's stats print

        # pkmn 1 fainted, pkmn 2 alive
        else:
            
            print(">>", pokemon1.name, "fainted.") # fainted message
            print("")
            
            if pokemon1.revives != 0: # pkmn 1 still has available revives
                reviveYN = input("Would you like to use Revive? YES or NO: ").upper() # ask p1 to use revive
                print("")
                if reviveYN == "YES": # p1 wants to revive
                    pokemon1.revive(pokemon1) # revive pkmn1
                    pokemon1.revives -= 1 # minus 1 available revive
                else: # p1 does not want to revive
                    print(">>", pokemon2.name, "defeated", pokemon1.name + "!") # p2 defeated p1 message
                    win() # p2 wins message
                    gameplaying = False # while loop terminates, game ends
                    
            else: # pkmn 1 has no more revives
                print("No Revives remaining.")
                print("")
                print(">>", pokemon2.name, "defeated", pokemon1.name + "!") # p2 defeated p1 message
                win() # p2 wins message 
                gameplaying = False # while loop terminates, game ends
                
            continue

        # both pkmn alive
        if pokemon1.fainted == False and pokemon2.fainted == False:

            print("It is", pokemon2.name + "'s turn.") # turn message
            pokemon2.attack(pokemon1) # pkmn 2 attacks pkmn 1
            pokemon1.printStats() # print pkmn 1 stats

        # pkmn 1 alive, pkmn 2 fainted
        else:
            
            print(">>", pokemon2.name, "fainted.") # fainted message
            print("")
            
            if pokemon2.revives != 0: # pkmn 2 still has available revives
                reviveYN = input("Would you like to use Revive? YES or NO: ").upper() # ask p2 to use revive
                print("")
                if reviveYN == "YES": # p2 wants to revive
                    pokemon2.revive(pokemon1) # revive pkmn2
                    pokemon2.revives -= 1 # minus 1 available revive
                else: # p2 does not want to revive
                    print(">>", pokemon1.name, "defeated", pokemon2.name + "!") # p1 defeated p2 message
                    win() # p1 wins message
                    gameplaying = False # while loop terminates, game ends
                    
            else: # pkmn 2 has no more revives
                print("No Revives remaining.")
                print("")
                print(">>", pokemon1.name, "defeated", pokemon2.name + "!") # p1 defeated p2 message
                win() # p1 wins message
                gameplaying = False # while loop terminates, game ends
                
            continue        
        
# MAIN FUNCTION

def main():
    
    playingpokemon = setup() # call setup() function, define variable for returned value of list of 2 pkmn
    battle(playingpokemon) # call battle() function on list of 2 pkmn
    
if __name__ == "__main__":
    main()

# ------------------------------------------------------
# REFERENCES:
# Consulted Caitlin Ong.
