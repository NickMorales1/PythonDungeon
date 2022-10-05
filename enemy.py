# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Individual Project enemy.py
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
Created on Tue Nov 24 22:53:23 2020

@author: nekom
"""
import random as r
import character

#################################################################
# MAIN CLASSES

class Enemy:
    def __init__(myEnemy,name,health,maxHealth,level,minDamage,maxDamage,missChance,critChance,statusEffect,statusLength,statusStrength,dead):
        """
        Basic Enemy class is the basis for all monsters in the game

        Parameters
        ----------
        myEnemy : TYPE
            DESCRIPTION.
        name : TYPE
            DESCRIPTION.
        health : TYPE
            DESCRIPTION.
        maxHealth : TYPE
            DESCRIPTION.
        level : TYPE
            DESCRIPTION.
        minDamage : TYPE
            DESCRIPTION.
        maxDamage : TYPE
            DESCRIPTION.
        missChance : TYPE
            DESCRIPTION.
        critChance : TYPE
            DESCRIPTION.
        statusEffect : TYPE
            DESCRIPTION.
        statusLength : TYPE
            DESCRIPTION.
        statusStrength : TYPE
            DESCRIPTION.
        dead : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        myEnemy.name = name
        myEnemy.health = health
        myEnemy.maxHealth = maxHealth
        myEnemy.level = level
        myEnemy.minDamage = minDamage
        myEnemy.maxDamage = maxDamage
        myEnemy.missChance = missChance
        myEnemy.critChance = critChance
        myEnemy.statusEffect = statusEffect
        myEnemy.statusLength = statusLength
        myEnemy.statusStrength = statusStrength
        myEnemy.dead = dead


#################################################################

#################################################################
# ENEMY

def createEnemy():
    """
    Function to create an enemy based on the players current level

    Returns
    -------
    enemy : TYPE
        DESCRIPTION.

    """
    global enemy
    name = genEnemyName()
    dead = False
    statusEffect = 'None'
    statusLength = -1
    statusStrength = 0
    level = genEnemyLevel(character.player.level)
    minDamage = genEnemyMinDamage(level)
    maxDamage = genEnemyMaxDamage(level)
    maxHealth = genEnemyMaxHealth(level)
    health = maxHealth
    missChance = 15
    critChance = 5
    enemy = Enemy(name,health,maxHealth,level,minDamage,maxDamage,missChance,critChance,statusEffect,statusLength,statusStrength,dead)
    return enemy


def genEnemyLevel(playerLevel):
    """
    Generates the enemy's level based on the current player's level

    Parameters
    ----------
    playerLevel : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    rng = r.randint(1,100)
    
    if(playerLevel == 1):
        if(rng >= 80):
            return 2
        else:
            return 1
    else:
        if(rng >= 75):
            return playerLevel + 1
        elif(rng <= 20):
            return playerLevel - 1
        else:
            return playerLevel
        
def genEnemyName():
    """
    Functions used in the generate enemy function for a random enemy name
    Initially the name was going to correlate to in-game stats, though this was
    never implemented in the final project

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    list = ['Death Dog','Earth Elemental','Cave Goblin','Ghoul','Harpy','Horned Devil','Hobgoblin',
            'Lich','Medusa','Minotaur','Ogre','Zombie','Skeleton','Troll','Winter Wolf']
    return r.choice(list)

def genEnemyBaseHealth(level):
    """
    Generates the enemy's base health before random modification

    Parameters
    ----------
    level : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if(level == 1):
      return 5
    elif(level == 2):
      return 12
    elif(level == 3):
      return 25
    elif(level == 4):
      return 35
    elif(level == 5):
      return 50
    elif(level == 6):
      return 60
    elif(level == 7):
      return 75
    elif(level == 8):
      return 85
    else:
      return 8 * level + 20
  
def genEnemyBonusHealth(level):
    """
    Randomly adds health to an enemy based on the player level

    Parameters
    ----------
    level : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if(level <= 3):
        return r.randint(1,3)
    else:
        return r.randint(1,5)
    
def genEnemyMaxHealth(level):
    """
    Combines the previous two functions to get the enemy's max health

    Parameters
    ----------
    level : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return genEnemyBaseHealth(level) + genEnemyBonusHealth(level)


def genEnemyMinDamage(level):
    """
    Generates the enemy's minimum damage

    Parameters
    ----------
    level : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return 2 * level
        
def genEnemyMaxDamage(level):
    """
    Generates the enemy's maximum damage output

    Parameters
    ----------
    level : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if(level == 1):
        return 4
    if(level == 2):
        return 6
    if(level == 3):
        return 9
    if(level == 4):
        return 12
    if(level == 5):
        return 20
    if(level == 6):
        return 25
    if(level == 7):
        return 30
    if(level == 8):
        return 40
    if(level >= 9):
        return level * 5
    
    
def viewEnemy():
    """
    Function that prints the enemy's stats

    Returns
    -------
    None.

    """
    global enemy
    print('-------------------------------------------------------------')
    print(f'Level {enemy.level} {enemy.name}')
    print(f' Current Health: {enemy.health}')
    print(f'Max Health: {enemy.maxHealth}')
    print('-------------------------------------------------------------')
    
def attack():
    """
    Randomly generates the damage the enemy does that turn

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    global enemy
    return r.randint(enemy.minDamage,enemy.maxDamage)


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