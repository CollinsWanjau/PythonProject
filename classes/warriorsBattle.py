# ----------------WARRIORS BATTLE------------
# We will create a game with this simple output
"""
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has died and Sam is Victorious
Game over
"""

# We will create a Warrior & Battle class

import random
import math

# Warriors will have names, health, and attack and block maximums
# They will have the capabilities to attack and block random amounts

# Attack random() 0.0 to 1.0 * maxAttack + .5

# Block will use random()

# Battle Class capability of looping until 1 warrior dies
# Warriors will each get a turn to attack each other

# Function gets 2 warriors
# 1 warrior attacks the  other
# Attacks and Blocks be integers

class Warrior:
    def __init__(self, name="warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax
    def attack(self):
        attAmt = self.attkMax * (random.random() + .5)
        return attAmt
    def block(self):
        blckAmt = self.blockMax * (random.random() + .5)
        return blckAmt
class Battle:
    def startFight(self, warrior1, warrior2):
        # continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.getAttackResult(warrior2, warrior1) == "Game over":
                print("Game over")
                break
            if self.getAttackResult(warrior1, warrior2) == "Game over":
                print("Game over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAattAmt = warriorA.attack()
        warriorBblckAmt = warriorB.block()
        damage2warriorB = math.ceil(warriorAattAmt - warriorBblckAmt)
        warriorB.health = warriorB.health - damage2warriorB
        if damage2warriorB < 0:
            damage2warriorB = 0
            warriorB.health = warriorB.health - damage2warriorB
        if warriorB.health < 0:
            warriorB.health = 0
        print("{} attacks {} and deals {} damage".format(warriorA.name,
            warriorB.name, damage2warriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))




        if warriorB.health <= 0:
            print("{} has died and {} is Victorious".format \
                    (warriorB.name, warriorA.name))
            return "Game over"
        else:
            return "Fight Again"

def main():
    # create 2 Warriors
    paul = Warrior("paul", 50, 20, 10)
    sam = Warrior("sam", 50, 20, 10)

    # Create battle object
    battle = Battle()

    # Initiate Battle
    battle.startFight(paul, sam)
main()

