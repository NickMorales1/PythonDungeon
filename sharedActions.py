# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Individual Project sharedActions.py
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
Created on Tue Nov 24 23:07:51 2020

@author: nekom
"""
import random as r



#################################################################
# SHARED ACTIONS

def ifDead(player):
    """
    Checks if the input player is dead and changes their dead value

    Parameters
    ----------
    player : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if(player.health == 0):
        player.dead = True
    else:
        player.dead = False

def takeDamage(player,damageTaken):
    """
    Deals the damage to the given player of the given amount

    Parameters
    ----------
    player : TYPE
        DESCRIPTION.
    damageTaken : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if(player.health - damageTaken < 0):
            player.health = 0
            ifDead(player)
    else:
        player.health = player.health - damageTaken
    
    
def heal(player,healing):
    """
    Heals the player a given amount

    Parameters
    ----------
    player : TYPE
        DESCRIPTION.
    healing : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if(player.health + healing > player.maxHealth):
        player.health = player.maxHealth
    else:
        player.health = player.health + healing
        

        
        
    
def doesHit(attacker):
    """
    Checks if the attacker hits their attack

    Parameters
    ----------
    attacker : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    missChance = attacker.missChance
    if(r.randint(1,100) > missChance):
        return True
    else:
        return False
    
def doesCrit(attacker):
    """
    Checks if the attacker hits a critical attack

    Parameters
    ----------
    attacker : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    critChance = attacker.critChance
    if(r.randint(1,100) < critChance):
        return True
    else:
        return False
    

        
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