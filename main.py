# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Individual Project main.py
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
Created on Fri Nov  6 23:52:27 2020

@author: nekom
"""

import map
import character
import enemy
import sharedActions

import random as r
import math as m



#################################################################
# PRE GAME FUNCTIONS

    
def doStatusEffect(player):
    """
    Initially implemented so it could work with whatever status effect an enemy had
    However, in the final version of the game the only status effect an enemy can
    obtain is poison, but this function does the damage of the poison at the 
    beginning of each turn
    

    Parameters
    ----------
    player : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if(player.statusEffect == 'poison'):
        sharedActions.takeDamage(player,player.statusStrength)
        player.statusStrength = int(player.statusStrength/2)
    
    player.statusLength -= 1
    if(player.statusLength == 0 or player.statusStrenth == 0):
        player.statusEffect = 'none'
        player.statusStrength = 0
        player.statusLength = -1
    
    pass

    
def useItem(itemType,strength):
    """
    Uses the item that is selected

    Parameters
    ----------
    itemType : TYPE
        DESCRIPTION.
    strength : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    if(itemType == 'heal)'):
        sharedActions.heal(player, strength)
    elif(itemType == 'Poison'):
        doStatusEffect(monster)
        pass
    
def println():
    """
    Quality of life function created near the end of the production to make
    an originally java programmer more at ease with printing blank lines

    Returns
    -------
    None.

    """
    print('')



def devMode():
    """
    The hub of console commands used to help debug and program this
    I am not responsible for the results created as a result of using such
    commands

    Returns
    -------
    None.

    """
    code = input('Input the code: ')
    if(code == 'motherlode'):
        character.gainGold(50000)
    elif(code == 'hp'):
        player.health = player.maxHealth
    elif(code == 'lvlup'):
        xp = character.xpToNextLevel()
        character.gainXP(xp)
        if(character.canLevelUp()):
                    character.levelUp()
                    player.maxHealth = int(1.25*m.pow(player.level,2) + 20)
                    player.health = player.maxHealth
                    player.critChance += 5
                    print('You have leveled up!')
                    print(f'You are now level {player.level}')
                    println()
    elif(code == 'time2die'):
        global currentWeapon
        currentWeapon = character.giveDevWeapon()
    elif(code == 'allthehp'):
        character.maxHealth = 999
        character.health = character.maxHealth
    println()
        
    
#################################################################


#################################################################
#GAME START

print('Dungeon Grid Key:')
print('0 - Empty Room')
print('1 - Player Location')
print('2 - Wall (Cannot Enter)')
print('3 - Shop')
print('9 - Cleared Room')
##############################################################################
#CREATE PLAYER MAP
map.create_map()
map.create_walls()
map.create_shop()
map.set_initial_position()
##############################################################################


##############################################################################
#CREATE INITIAL PLAYER AND INVENTORY
player = character.createCharacter()


currentWeapon = character.giveInitialWeapon()


inventory = character.initializeInventory()




map.print_grid()

character.viewInventory()
##############################################################################

##############################################################################
#INITIALIZE GAME-WIDE VARIABLES
combatDamage = 0
totalDamage = 0
combatHeal = 0
totalHeal = 0
enemiesKilled = 0
##############################################################################


#################################################################
#ACTUAL GAME HERE
cont = True
while(cont):
    
    #POSSIBLE ACTIONS THE PLAYER CAN TAKE
    print('ACTIONS')
    print('1. View Current Map')
    print('2. Move Character')
    print('3. View Inventory')
    print('4. View Weapon')
    print('5. View Character')
    print('6. Use Item')
    print('7. Exit Game')
    
    
    
    choice  = int(input('Your Choice: '))
    
    #################################################################
    #DECISION TREE
    if(choice == 1 ):
        map.print_grid()
    if(choice == 2):
        map.move_character()
    if(choice == 3):
        character.viewInventory()
    if(choice == 4):
        character.viewCurrentWeapon()
    if(choice == 5):
        character.viewCharacter()
    if(choice == 7):
        confirm = input('Are you sure you want to exit? (Y/N): ')
        if(confirm == 'Y'):
            cont = False
            break
        
        
    if(choice == 6):
                        
        character.viewInventory()
        available = False
        usingItem = True
        while(not(available)):
            print('If you do not want to use an item, type 9')
            itemChoice = int(input('Choose an item to use: '))
            if(itemChoice == 9):
                usingItem = False
                available = True
            elif(inventory[itemChoice-1].amount == 0):
                available = False
                print('You do not have any of that type of item')
            elif(inventory[itemChoice  - 1].effect == 'poison'):
                print('You cannot use a poison potion outside of battle')
            else:
                available = True
                                
                                
        #USING ITEM   
        if(usingItem):
            if(inventory[itemChoice - 1].effect == 'heal'):
                sharedActions.heal(player, inventory[itemChoice - 1].strength)
                #not yet created stun and agility potion effects
                
        
        
        
    if(choice == 31415):
        devMode()
        
     #################################################################   
        
        
        
        
    #IF THE CHARACTER MOVED INTO A NEW ROOM    
    if(choice == 2):
        roomType = map.get_room_type_str()
        
        #IF THE ROOM CONTAINS A MONSTER
        if(roomType == 'combat'):
            monster = enemy.createEnemy()
            
            print('---------------------------------------------------------------------------------')
            print(f'You have encountered a level {monster.level} {monster.name} with {monster.maxHealth} HP')
            print('---------------------------------------------------------------------------------')
            println()
            
            
            #CHECK FOR BOTH PLAYERS BEING ALIVE
            while(player.dead == False and monster.dead == False):
                if(monster.health == 0):
                    monster.dead = True
                sharedActions.ifDead(player)
                sharedActions.ifDead(monster)
                
                #INITIAL COMBAT ACTION IS FALSE UNLESS MONSTER DIES TO POISON
                combatAction = False
                
                #################################################################
                #SETUP POISON DAMAGE TAKEN AND PRINTOUT
                if(monster.statusEffect == 'poison'):
                    
                    sharedActions.takeDamage(monster, monster.statusStrength)
                    sharedActions.ifDead(monster)
                    print(f'The {monster.name} has taken {monster.statusStrength} poison damage')
                    monster.statusStrength = int(monster.statusStrength/2)  
                    if(monster.statusStrength == 0):
                        monster.statusEffect = 'none'
                        print(f'The poison has worn off of the {monster.name}')
                    if(monster.dead):
                        print(f'The {monster.name} has died to poison damage')
                        #ENDS UNNECCESARY PLAYER ACTION
                        combatAction = True
                #################################################################
                    
                #################################################################
                #PLAYER ACTION
                while(combatAction == False):
                    
                    print('-------------------------------------------------------------')
                    print('ACTIONS')
                    print('1. Attack')
                    print('2. Use Item')
                    print('3. View Inventory')
                    print('4. View Enemy')
                    print('5. View Weapon')
                    print('6. View Character')
                    print('-------------------------------------------------------------')
                    print('')
                    
                    combatChoice = int(input('What Will You Do: '))
                    
                    #ATTACK
                    if(combatChoice == 1):
                        
                        damageDone = character.dealDamage()
                        if(sharedActions.doesCrit(player)):
                            damageDone = 2 * damageDone
                            print('Critical Hit!')
                        sharedActions.takeDamage(monster,damageDone)
                        
                        combatDamage += damageDone
                        print(f'You have dealt {damageDone} damage')
                        
                        combatAction = True
                        
                    #ITEM SELECT    
                    if(combatChoice == 2):
                        
                        character.viewInventory()
                        available = False
                        usingItem = True
                        while(not(available)):
                            print('If you do not want to use an item, type 9')
                            itemChoice = int(input('Choose an item to use: '))
                            if(itemChoice == 9):
                                usingItem = False
                                available = True
                            elif(inventory[itemChoice-1].amount == 0):
                                available = False
                                print('You do not have any of that type of item')
                            else:
                                available = True
                                
                                
                        #USING ITEM   
                        if(usingItem):
                            if(inventory[itemChoice - 1].effect == 'poison'):
                                monster.statusEffect = inventory[itemChoice - 1].effect
                                monster.statusStrength = inventory[itemChoice - 1].strength
                            elif(inventory[itemChoice - 1].effect == 'heal'):
                                sharedActions.heal(player, inventory[itemChoice - 1].strength)
                        #not yet created stun and agility potion effects
                        combatAction = True
                    
                    #VIEW INVENTORY
                    if(combatChoice == 3):
                        character.viewInventory()
                        combatAction = False
                        
                    #VIEW ENEMY
                    if(combatChoice == 4):
                        enemy.viewEnemy()
                        combatAction = False
                        
                    #VIEW WEAPON
                    if(combatChoice == 5):
                        character.viewWeapon(currentWeapon)
                        
                    #VIEW CHARACTER
                    if(combatChoice == 6):
                        character.viewCharacter()
                
                # ENEMY ACTION
                if(not(monster.dead)):
                    if(sharedActions.doesHit(monster)):
                        damage = enemy.attack()
                        sharedActions.takeDamage(player, damage)
                        print(f'The {monster.name} dealt {damage} damage')
                    else:
                        print(f'The {monster.name} missed their attack')
                
                
                
            #POST COMBAT - ENEMY WINS
            if(player.dead):
                print('You have died')
                print(f'Current Level: {player.level}')
                print(f'Current Gold: {player.gold}')
                print(f'Current XP: {player.xp}')
                print(f'Total Enemies Killed: {enemiesKilled}')
                print(f'Total Damage Done: {totalDamage}')
                print(f'Total Healing: {totalHeal}')
                cont = False
                
                
                
                
            #POST COMBAT - PLAYER WINS
            if(monster.dead):
                println()
                print(f'You have killed the {monster.name}')
                println()
                enemiesKilled += 1
                
                totalDamage += combatDamage
                            
                totalHeal += combatHeal
                            
                goldGain = character.determineGoldGain(combatDamage,combatHeal)
                xpGain = character.determineXPGain(combatDamage,combatHeal)
                character.gainGold(goldGain)
                character.gainXP(xpGain)
                            
                print(f'You have gained {goldGain} gold and {xpGain} xp')
                
                #LEVEL-UP CHECK AND REWARDS
                if(character.canLevelUp()):
                    character.levelUp()
                    player.maxHealth = int(1.25*m.pow(player.level,2) + 20)
                    player.health = player.maxHealth
                    player.critChance += 5
                    print('You have leveled up!')
                    print(f'You are now level {player.level}')
                    println()
                    
                                
                    #NEED TO IMPLEMENT PLAYER STAT BONUSES HERE
                combatHeal = 0
                combatDamage = 0
                
                # ROOM LOOTING MECHANICS
                print('You Can Loot From This Room:')
                print('1. Gold')
                print('2. Item')
                print('3. Weapon')
                lootChoice = int((input('What do you want to loot from the room: ')))
                
                if(lootChoice == 1):
                    lootedGold = character.lootGold()
                    if(lootedGold == 1000):
                        print('You found a jackpot! 1000 Gold')
                    else:
                        print(f'You found {lootedGold} gold')
                    character.gainGold(lootedGold)
                if(lootChoice == 2):
                    
                    #CONTROLS WHAT ITEMS CAN BE LOOTED, REMOVED STUN AND AGILITY POTIONS
                    randomItem = r.randint(0,4)
                    print(f'You found a {inventory[randomItem].name}')
                    inventory[randomItem].amount += 1
                if(lootChoice == 3):
                    newWeapon = character.generateWeapon()
                    character.compareWeapons(currentWeapon,newWeapon)
                    character.swapWeapons(currentWeapon,newWeapon)
                map.make_empty_room()
              
                
        #################################################################        
        #ENTER STORE
        if(roomType == 'store'):
            wantToBuy = True
            #ALLOWS PLAYER TO BUY MULTIPLE DIFFERENT ITEMS
            while(wantToBuy):
            
                canBuy = False
                while(not(canBuy)):
                    print(f'Current Gold: {player.gold}')
                    print(f'Current Health: {player.health}')
                    print(f'Current Max Health: {player.maxHealth}')
                    print(f'1. Small Health Potion | Cost: {inventory[0].value} | Currently Own: {inventory[0].amount}')
                    print(f'2. Medium Health Potion | Cost: {inventory[1].value} | Currently Own: {inventory[1].amount}')
                    print(f'3. Large Health Potion | Cost: {inventory[2].value} | Currently Own: {inventory[2].amount}')
                    print(f'4. Small Poison Potion | Cost: {inventory[3].value} | Currently Own: {inventory[3].amount}')
                    print(f'5. Large Poison Potion | Cost: {inventory[4].value} | Currently Own: {inventory[4].amount}')
                    #print(f'6. Small Health Potion | Cost: {inventory[5].value} CURRENTLY UNUSABLE')
                    #print(f'7. Small Health Potion | Cost: {inventory[6].value} CURRENTLY UNUSABLE')
                    print('8. Leave the Store')
                    storeChoice = int(input('What Would you Like to Purchase From the Store: '))
                    println()
                    if(storeChoice == 8):
                        wantToBuy = False
                        canBuy = True
                    elif(storeChoice != 8):
                        itemCount = abs(int(input(f'How many {inventory[storeChoice - 1].name}s would you like to buy: ')))
                    
                        #CHECK IF PLAYER CAN BUY ITEM
                        if(player.gold > inventory[storeChoice - 1].value*itemCount):
                            #PLAYER BUYS ONE ITEM
                            if(itemCount == 1):
                                print(f'You have purchased a {inventory[storeChoice - 1].name}')
                                inventory[storeChoice - 1].amount += itemCount
                                character.spendGold(inventory[storeChoice - 1].value*itemCount)
                                canBuy = True
                            #PLAYER BUYS MULTIPLE OF ONE ITEM
                            elif(itemCount > 1):
                                print(f'You have purchased {itemCount} {inventory[storeChoice - 1].name}s')
                                inventory[storeChoice - 1].amount += itemCount
                                character.spendGold(inventory[storeChoice - 1].value*itemCount)
                                canBuy = True
                            else:
                                #PLAYER CANNOT BUY ITEM
                                if(itemCount == 1):
                                    print(f'You have insufficient gold to purchase a {inventory[storeChoice - 1].name}')
                                elif(itemCount > 1):
                                    print(f'You have insufficient gold to purchase {itemCount} {inventory[storeChoice - 1].name}s')
                                   
                            #CHECKS IF PLAYER WANTS TO STAY IN STORE
                            buyMore = ''
                            while(buyMore != 'Y' and buyMore != 'N'):
                                print(f'You have {player.gold} gold')
                                buyMore = input('Do you want to buy more? (Y/N): ')
                                if(buyMore == 'Y'):
                                    wantToBuy = True
                                elif(buyMore == 'N'):
                                    wantToBuy = False
        #ENTER AN EMPTY ROOM
        if(roomType == 'empty'):
            print('You have already killed the monster in this room')
            
        #ENDGAME, BEATEN ALL ROOMS, CHECKS IF PLAYER WANTS TO CONTINUE IN NEW DUNGEON
        if(map.map_is_clear()):
            print('You have defeated all monsters in this dungeon!')
            print('If you want, you may continue with your current player into a new dungeon')
            newChoice = ''
            while(newChoice != 'Y' and newChoice != 'N'):
                newChoice = input('Do you want to continue? (Y/N)')
            if(newChoice == 'N'):
                #ENDS GAME
                cont = False
            if(newChoice == 'Y'):
                #CREATES NEW DUNGEON
                map.create_map()
                map.create_walls()
                map.create_shop()
                map.set_initial_position()
                map.print_grid()                
                
                
#################################################################       
#CURRENT BUGS
#CLEAR

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''