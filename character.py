# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Individual Project character.py 
	Author:         Nicolas Morales, moral116@purdue.edu
	Team ID:        LC1-06
	
Contributors:   
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
"""
Created on Fri Nov  6 23:26:33 2020

@author: nekom

character.py
Creates and deals with character actions


"""
import random as r

#The XP Requirements for Each Level
#Is Insane at levels 17 and 18 because of testing
levelReq = [0,200,500,1000,2000,3000,5000,10000,15000,20000,25000,32000,40000,50000,100000,200000,1000000,99999999999999]

#################################################################
# MAIN CLASSES

class Character:
    def __init__(myChar,name,health,maxHealth,gold,level,xp,statusEffect,critChance,dead):
        """
        

        Parameters
        ----------
        myChar : TYPE
            DESCRIPTION.
        name : TYPE
            str.
        health : TYPE
            int.
        maxHealth : TYPE
            int.
        gold : TYPE
            int.
        level : TYPE
            int.
        xp : TYPE
            int.
        statusEffect : TYPE
            str.
        critChance : TYPE
            int.
        dead : TYPE
            int.

        Returns
        -------
        None.

        """
        myChar.name = name
        myChar.health = health
        myChar.maxHealth = maxHealth
        myChar.gold = gold
        myChar.level = level
        myChar.xp = xp
        myChar.statusEffect = statusEffect
        myChar.critChance = critChance
        myChar.dead = dead
        
        
    
class Weapon:
    def __init__(myWeapon,name,damage,levelReq,diceNum,dicePower):
        """
        

        Parameters
        ----------
        myWeapon : TYPE
            DESCRIPTION.
        name : TYPE
            str.
        damage : TYPE
            int.
        levelReq : TYPE
            int.
        diceNum : TYPE
            int.
        dicePower : TYPE
            int.

        Returns
        -------
        None.

        """
        myWeapon.name = name
        myWeapon.damage = damage
        myWeapon.levelReq = levelReq
        myWeapon.diceNum = diceNum
        myWeapon.dicePower = dicePower
 
        
 
        
        
class Item:
    def __init__(myItem,name,amount,effect,strength,value):
        """
        

        Parameters
        ----------
        myItem : TYPE
            DESCRIPTION.
        name : TYPE
            str.
        amount : TYPE
            int.
        effect : TYPE
            str.
        strength : TYPE
            int.
        value : TYPE
            int.

        Returns
        -------
        None.

        """
        myItem.name = name
        myItem.amount = amount
        myItem.effect = effect
        myItem.strength = strength
        myItem.value = value
     
        


        

#################################################################

#################################################################
# PLAYER ACTIONS


def createCharacter():
    """
    Initially creates the character with level 1 stats

    Returns
    -------
    player : TYPE
        DESCRIPTION.

    """
    #myChar,name,health,maxHealth,gold,level,xp,statusEffect,critChance,dead
    global player
    name = input('Input your name: ')
    player = Character(name,20,20,0,1,0,'none',20,False)
    return player
    pass



        
def gainGold(goldGain):
    """
    Adds gold to a players account

    Parameters
    ----------
    goldGain : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    global player
    player.gold += goldGain
    
def spendGold(spendGold):
    """
    Takes gold from a players account

    Parameters
    ----------
    spendGold : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    global player
    player.gold -= spendGold


def gainXP(xpGain):
    """
    Gives a player xp

    Parameters
    ----------
    xpGain : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    global player
    player.xp += xpGain

def levelUp():
    """
    Levels up a character

    Returns
    -------
    None.

    """
    global player
    player.level += 1
    
def canLevelUp():
    """
    Checks if a player can level up with current xp level

    Returns
    -------
    bool
        DESCRIPTION.

    """
    global player
    global levelReq
    #levelReq = [0,200,500,1000,2000,3000,5000,10000,15000]
    if(player.xp >= levelReq[player.level]):
        return True
    else:
        return False
    
def xpToNextLevel():
    """
    Returns xp to next level in int form

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    global player
    global levelReq
    return levelReq[player.level] - player.xp

def viewCharacter():
    """
    Prints a characters information

    Returns
    -------
    None.

    """
    global player
    nextxp = xpToNextLevel()
    print('-------------------------------------------------------------')
    print(f'{player.name}')
    print(f'Current Level: {player.level}')
    print(f'Gold: {player.gold}')
    print(f'XP: {player.xp}')
    print(f'XP To Next Level: {nextxp}')
    print(f'Current Health: {player.health}')
    print(f'Max Health: {player.maxHealth}')
    print('-------------------------------------------------------------')
    print()


def determineGoldGain(combatDamage,combatHeal):
    """
    Determines how much gold the character gets from each battle, some randomness
    included

    Parameters
    ----------
    combatDamage : TYPE
        DESCRIPTION.
    combatHeal : TYPE
        DESCRIPTION.

    Returns
    -------
    gold : TYPE
        DESCRIPTION.

    """
    gold = 0
    gold += 5*player.level
    gold += int(combatDamage*1.2 + combatHeal*.75)
    gold += r.randint(0,3*player.level)
    return gold

def determineXPGain(combatDamage,combatHeal):
    """
    Determines how much xp the character gains from battle, some variability

    Parameters
    ----------
    combatDamage : TYPE
        DESCRIPTION.
    combatHeal : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    xp  = 0
    xp += 10*player.level
    xp += 5*combatDamage + 3*combatHeal
    xp += r.randint(0,7*player.level)
    return xp
    

def lootGold():
    """
    Calculates and returns the amount of gold looted from a room if chosen
    Small chance of finding a jackpot

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    gold = 0
    jackpot = r.randint(1,100)
    if(jackpot == 50):
        
        return 1000
    
    gold += 4*player.level
    multiplier = r.randint(7,20)
    gold += r.randint(5,player.level*multiplier)
    return gold
    

#################################################################        

#################################################################
# WEAPON

def viewWeapon(weapon):
    """
    Prints basic info on weapon

    Parameters
    ----------
    weapon : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print(f'Current Weapon: {weapon.name}\n')
    print(f'Weapon Dice: {weapon.damage}\n')
    print(f'Weapon Level Requirement: {weapon.levelReq}\n')
    
def viewCurrentWeapon():
    """
    Prints basic information on the players current weapon

    Returns
    -------
    None.

    """
    global currentWeapon
    print(f'Current Weapon: {currentWeapon.name}\n')
    print(f'Weapon Dice: {currentWeapon.damage}\n')
    print(f'Weapon Level Requirement: {currentWeapon.levelReq}\n')
    
    

def giveInitialWeapon():
    """
    Gives the player the first weapon

    Returns
    -------
    currentWeapon : TYPE
        DESCRIPTION.

    """
    global currentWeapon
    currentWeapon = Weapon('Training Sword','1d6',1,1,6)
    return currentWeapon


def giveDevWeapon():
    """
    Testing weapon used to make sure endgame works correctly

    Returns
    -------
    currentWeapon : TYPE
        DESCRIPTION.

    """
    global currentWeapon;
    currentWeapon = Weapon('God Mode','1shotall',1,20,1)
    return currentWeapon




def compareWeapons(weapon,newWeapon):
    """
    Compares a players current weapon with another one

    Parameters
    ----------
    weapon : TYPE
        DESCRIPTION.
    newWeapon : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    global currentWeapon
    print('-------------------------------------------------------------')
    print('Current Weapon:')
    viewWeapon(currentWeapon)
    print('-------------------------------------------------------------')
    print('New Weapon: ')
    viewWeapon(newWeapon)
    print('-------------------------------------------------------------')
    
def swapWeapons(weapon,newWeapon):
    """
    Swaps a players current weapon with a found one

    Parameters
    ----------
    weapon : TYPE
        DESCRIPTION.
    newWeapon : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    global currentWeapon
    check = input('Do you want the new weapon: (Y/N) ')
    if(check == 'Y'):
        currentWeapon = newWeapon
        print('You have chosen the new weapon')
    else:
        print('You have kept your old weapon')
        
def dealDamage():
    """
    Determines how much damage a character does using dice mechanics

    Returns
    -------
    damage : TYPE
        DESCRIPTION.

    """
    global currentWeapon
    i = 0
    damage = 0
    #print(f'Dice Power: {currentWeapon.dicePower}')
    while(i < currentWeapon.diceNum):
        damage += damage + r.randint(1,currentWeapon.dicePower)
        #print(f'{damage}')
        i += 1
    
    return damage
    
# GENERATE WEAPON
#myWeapon,name,damage,levelReq,diceNum,dicePower

def generateWeapon():
    """
    Generates a weapon that the player can loot
    Name is random and stats are partially random but also dependent on level
    Hint: Dice Number upgrades occur at levels 3,5,8

    Returns
    -------
    weapon : TYPE
        DESCRIPTION.

    """
    name = genWeaponName()
    levelReq = player.level
    diceNum = int(player.level*.4 + 1)
    powerPoss = [6,8,12,20]
    dicePower = r.choice(powerPoss)
    damage = str(diceNum)+ 'd' + str(dicePower)
    weapon = Weapon(name,damage,levelReq,diceNum,dicePower)
    return weapon
   

    
def genWeaponName():
    """
    Generates a random weapon name to be used in the creation of a weapon
    Initially there was going to be the chance of a rare weapon, however time 
    constraints limited those efforts

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    list = ['Bronze Shortsword','Battle Axe','Claymore','Cursed Broadsword','Cutlass','Morning Star','Rusty Cleaver','Mace','War Hammer','Iron Flail',
            'Twin Daggers','Officer\'s Blade','Steel Maul','Steel Rapier']
    return r.choice(list)



#################################################################

#################################################################
# ITEMS

def initializeInventory():
    """
    Creates the players inventory with basic equipment
    Side Note: A Stun and Agility Potion were both initially implemented, though
    due to time constrains led to their deletion from the final product

    Returns
    -------
    inventory : TYPE
        DESCRIPTION.

    """
    global inventory
    inventory = []
    smallHeal = Item('Small Healing Potion',0,'heal',10,20)
    mediumHeal = Item('Medium Healing Potion',0,'heal',25,50)
    largeHeal = Item('Large Healing Potion',0,'heal',50,120)
    
    smallPoison = Item('Small Poison Potion',0,'poison',8,25)
    largePoison = Item('Large Poison Potion',0,'poison',18,75)
    
    #stunPotion = Item('Stun Potion',0,'stun',2,100)
    
    #agilityPotion = Item('Agility Potion',0,'dodge',5,200)
    
    inventory.append(smallHeal)
    inventory.append(mediumHeal)
    inventory.append(largeHeal)
    
    inventory.append(smallPoison)
    inventory.append(largePoison)
    
    #inventory.append(stunPotion)
    
    #inventory.append(agilityPotion)
    return inventory
    
    
#-----------------------------------------------------------------------------
# INVENTORY ITEM INDICES
#
# 0 - Small Healing Potion
# 1 - Medium Healing Potion
# 2 - Large Healing Potion
# 3 - Small Poison Potion
# 4 - Large Poison Potion
# 5 - Stun Potion
# 6 - Agility Potion
#-----------------------------------------------------------------------------


# VIEW INVENTORY

def viewInventory():
    """
    Basic function to print all of the items in the players inventory

    Returns
    -------
    None.

    """
    global inventory
    j = 1
    print('INVENTORY')
    print('-------------------------------------------------------------')
    for i in inventory:
        #if(i.amount > 0):
            print(f'{j}.')
            print(f'{i.name}')
            print(f'Count: {i.amount}')
            print(f'Strength: {i.strength}')
            print(f'Type: {i.effect}')
            print(f'Value: {i.value}')
            print()
            j += 1
    print('-------------------------------------------------------------')

#################################################################

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''