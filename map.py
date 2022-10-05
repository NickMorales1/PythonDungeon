# -*- coding: utf-8 -*-

'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Individual Project map.py
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
Created on Fri Nov  6 00:40:23 2020

@author: nekom

map.py
This file creates the dungeon space with walls, and can move the character between rooms


"""

import numpy as np
import random



#################################################################
# CREATE MAP AND OBJECTS


'''
Dungeon Grid Key:
0 - Empty Room
1 - Player Location
2 - Wall (Cannot Enter)
3 - Shop
9 - Cleared Room
'''


'''
Do this first and don't do again, will delete the character's previous position and walls
'''
def create_map():
    """
    Creates Blank Map

    Returns
    -------
    None.

    """
    global grid
    global rows
    global cols
    
    
    grid = np.zeros(50).reshape(5,10)
    rows = grid.shape[0]
    cols = grid.shape[1]




def create_walls():
    """
    Randomly generates walls within the map, impassable by the character

    Returns
    -------
    None.

    """
    global grid
    for x in range(1,cols-1):
        for y in range(1,rows-1):
           
            if((grid[y-1][x-1] and grid[y-1][x] and grid[y-1][x+1] and grid[y][x-1] and grid[y][x+1] and grid[y+1][x-1] and grid[y+1][x] and grid[y+1][x+1]) != 2):
               if(random.randrange(9) <= 1):
                   grid[y][x] = 2
               
def create_shop():
    """
    Creates a shop in a random open location on the map

    Returns
    -------
    None.

    """
    global grid
    global y_shop
    global x_shop
    y_shop = -1
    x_shop = -1
    shopExist = False
    while(not(shopExist)):
        y_shop = random.randint(0,4)
        x_shop = random.randint(0,9)
        if(grid[y_shop][x_shop] == 0):
            grid[y_shop][x_shop] = 3
            shopExist = True
                
                
#################################################################


#################################################################
#CHECK IF MAP IS CLEAR OF MONSTERS
def map_is_clear():
    """
    Checks if the map is clear or all monsters, returns true if clear

    Returns
    -------
    bool
        DESCRIPTION.

    """
    
    global grid
    for x in range(1,cols-1):
        for y in range(1,rows-1):
            if(grid[y][x] == 0):
                return False
    return True
    


#################################################################


#################################################################
# SET PLAYER INITIAL POSITION
               
"""
player's initial position
position is in the format [y,x]
Top Left [0,0]
Bottom Right [4,9]

"""


def set_initial_position():
    """
    Sets the player initial position, is constant

    Returns
    -------
    None.

    """
    global player_x_pos
    global player_y_pos
    global grid
    global current_Room_Type
    global new_Room_Type
    player_x_pos = -1
    player_y_pos = -1
    grid[4,2] = 1
    current_Room_Type = 0
    new_Room_Type = -1

    
#################################################################
  
#################################################################
# PRINT MAP

def print_grid():
    """
    Prints the current map layout to the screen

    Returns
    -------
    None.

    """
    print()
    print('The Dungeon')
    print(grid)
    print()
    
    
#################################################################

#################################################################
# UPDATE PLAYER POSITION

def update_player_pos():
    """
    Updates the player's position coordinates

    Returns
    -------
    None.

    """
    global player_x_pos
    global player_y_pos
    
    for x in range(0,cols):
        for y in range(0,rows):
            if((grid[y,x]) == 1):
                player_x_pos = x
                player_y_pos = y

#################################################################

#################################################################
# GET SQUARE TYPE

def get_north_pos():
    """
    Returns the grid position of the space above the character

    Returns
    -------
    TYPE
        DESCRIPTION.
        grid position

    """
    global player_x_pos
    global player_y_pos
    return grid[player_y_pos - 1][player_x_pos]

def get_south_pos():
    """
    Returns the grid position of the space below the character

    Returns
    -------
    TYPE
        DESCRIPTION.
        grid position

    """
    global player_x_pos
    global player_y_pos
    return grid[player_y_pos + 1][player_x_pos]


def get_west_pos():
    """
    Returns the grid position of the space to the left of the character

    Returns
    -------
    TYPE
        DESCRIPTION.
        grid position

    """
    global player_x_pos
    global player_y_pos
    return grid[player_y_pos][player_x_pos - 1]

def get_east_pos():
    """
    Returns the grid position of the space to the right of the character

    Returns
    -------
    TYPE
        DESCRIPTION.
        grid position

    """
    global player_x_pos
    global player_y_pos
    return grid[player_y_pos][player_x_pos + 1]


def get_room_type():
    """
    Returns the type of the room in int form

    Returns
    -------
    current_Room_Type : TYPE
        DESCRIPTION.
        int

    """
    global current_Room_Type
    return current_Room_Type

def get_room_type_str():
    """
    Converts the int room type to string
    Wall not included because movement checks are done by above functions and
    this function is only used for player's position

    Returns
    -------
    str
        DESCRIPTION.

    """
    room = get_room_type()
    if(room == 0):
        return 'combat'
    if(room == 3):
        return 'store'
    if(room == 9):
        return 'empty'
    
def make_empty_room():
    global current_Room_Type
    current_Room_Type = 9

#################################################################


#################################################################
# MOVEMENT CHECKS

def can_move_up():
    """
    Checks if the player can move to the space above them

    Returns
    -------
    bool
        DESCRIPTION.

    """
    global player_x_pos
    global player_y_pos
    if(player_y_pos == 0):
        return False
    elif(get_north_pos() == 2):
        return False
    else:
        return True
    
def can_move_down():
    """
    Checks if the player can move to the space below them

    Returns
    -------
    bool
        DESCRIPTION.
        """
    global rows
    global player_x_pos
    global player_y_pos
    if(player_y_pos == rows - 1):
        return False
    elif(get_south_pos() == 2):
        return False
    else:
        return True
    
def can_move_left():
    """
    Checks if the player can move to the space to the left of them

    Returns
    -------
    bool
        DESCRIPTION.

    """
    global player_x_pos
    global player_y_pos
    if(player_x_pos == 0):
        return False
    elif(get_west_pos() == 2):
        return False
    else:
        return True
    
def can_move_right():
    """
    Checks if the player can move the space to the right of them

    Returns
    -------
    bool
        DESCRIPTION.

    """
    global player_x_pos
    global player_y_pos
    global cols
    if(player_x_pos == cols - 1):
        return False
    if(get_east_pos() == 2):
        return False
    else:
        return True
    
#################################################################


#################################################################
# MOVEMENT
    
def move_up():
    """
    Moves the character up one space and updates both their current position
    and remembers the room type they are in to replace it when they leave

    Returns
    -------
    None.

    """
    global player_x_pos
    global player_y_pos
    global grid
    
    global new_Room_Type
    global current_Room_Type
    
    new_Room_Type = get_north_pos()
    grid[player_y_pos][player_x_pos] = current_Room_Type
    current_Room_Type = new_Room_Type
    grid[player_y_pos - 1][player_x_pos] = 1
    
    update_player_pos()
    print_grid()
    
    
def move_down():
    """
    Moves the character down one space and updates both their current position
    and remembers the room type they are in to replace it when they leave

    Returns
    -------
    None.

    """
    global player_x_pos
    global player_y_pos
    global grid
    
    global new_Room_Type
    global current_Room_Type
    
    new_Room_Type = get_south_pos()
    grid[player_y_pos][player_x_pos] = current_Room_Type
    current_Room_Type = new_Room_Type
    grid[player_y_pos + 1][player_x_pos] = 1
    
    update_player_pos()
    print_grid()
    
    
def move_left():
    """
    Moves the character left one space and updates both their current position
    and remembers the room type they are in to replace it when they leave

    Returns
    -------
    None.

    """
    global player_x_pos
    global player_y_pos
    global grid
    
    global new_Room_Type
    global current_Room_Type
    
    new_Room_Type = get_west_pos()
    grid[player_y_pos][player_x_pos] = current_Room_Type
    current_Room_Type = new_Room_Type
    grid[player_y_pos][player_x_pos - 1] = 1
    
    update_player_pos()
    print_grid()
    
    
def move_right():
    """
    Moves the character right one space and updates both their current position
    and remembers the room type they are in to replace it when they leave

    Returns
    -------
    None.

    """
    global player_x_pos
    global player_y_pos
    global grid
    
    global new_Room_Type
    global current_Room_Type
    
    new_Room_Type = get_east_pos()
    grid[player_y_pos][player_x_pos] = current_Room_Type
    current_Room_Type = new_Room_Type
    grid[player_y_pos][player_x_pos + 1] = 1
    
    update_player_pos()
    print_grid()
    
        
#################################################################   
    

#################################################################
# MOVE PLAYER

def move_character():
    """
    Main function of the map class that gives the player the choice where to move
    
    Movement numbers are adaptive depending on which direction the player can 
    move into

    Returns
    -------
    None.

    """
    
    cont = True
    option_numbers = [1,2,3,4,5,6,7,8]
    i = 0 
    move_up_number = -1
    move_down_number = -1
    move_left_number = -1
    move_right_number = -1


    while(cont):
        i = 0
        update_player_pos()
        print_grid()
        print('Where will you move?')
        print()
    
        #options = []
        if(can_move_up()):
            print(f'{option_numbers[i]}. Move Up')
            move_up_number = option_numbers[i]
            i+=1
        else:
            move_up_number = -1
        if(can_move_down()):
            print(f'{option_numbers[i]}. Move Down')
            move_down_number = option_numbers[i]
            i+=1
        else:
            move_down_number = -1
        if(can_move_left()):
            print(f'{option_numbers[i]}. Move Left')
            move_left_number = option_numbers[i]
            i+=1
        else:
            move_left_number = -1
        if(can_move_right()):
            print(f'{option_numbers[i]}. Move Right')
            move_right_number = option_numbers[i]
            i+=1
        else:
            move_right_number = -1
                                        
        print('9. Exit')
        exit_number = 9
                                        
                                        
        print()
        movement_choice = int(input('Your choice: '))
        while(movement_choice == -1):
            print('Invalid option')
            movement_choice = int(input('Your choice: '))
        while(movement_choice != move_up_number and movement_choice != move_down_number and movement_choice != move_left_number and movement_choice != move_right_number and movement_choice != exit_number):
            print('Invalid option')
            movement_choice = int(input('Your choice: '))
                                                
        if(movement_choice == move_up_number):
            move_up()
        elif(movement_choice == move_down_number):
            move_down()
        elif(movement_choice == move_left_number):
            move_left()
        elif(movement_choice == move_right_number):
            move_right()
        elif(movement_choice == exit_number):
            cont = False
        cont = False
        
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