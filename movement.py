# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:09:45 2020

@author: nekom
"""

'''
These four functions check if the player can move in the desired direction
'''

def can_move_up():
    global player_x_pos
    global player_y_pos
    if(player_y_pos == 0):
        return False
    elif(grid[player_y_pos - 1][player_x_pos] == 2):
        return False
    else:
        return True
    
def can_move_down():
    global rows
    global player_x_pos
    global player_y_pos
    if(player_y_pos == rows - 1):
        return False
    elif(grid[player_y_pos + 1][player_x_pos] == 2):
        return False
    else:
        return True
    
def can_move_left():
    global player_x_pos
    global player_y_pos
    if(player_x_pos == 0):
        return False
    elif(grid[player_y_pos][player_x_pos - 1] == 2):
        return False
    else:
        return True
    
def can_move_right():
    global cols
    global player_x_pos
    global player_y_pos
    if(player_x_pos == cols - 1):
        return False
    if(grid[player_y_pos][player_x_pos + 1] == 2):
        return False
    else:
        return True
    

'''
These next four functions actually move the character
'''
    
    
def move_up():
    global player_x_pos
    global player_y_pos
    global grid
    grid[player_y_pos - 1][player_x_pos] = 1
    grid[player_y_pos][player_x_pos] = 0
    update_player_pos()
    print_grid()
    
def move_down():
    global player_x_pos
    global player_y_pos
    global grid
    grid[player_y_pos + 1][player_x_pos] = 1
    grid[player_y_pos][player_x_pos] = 0
    update_player_pos()
    print_grid()
    
def move_left():
    global player_x_pos
    global player_y_pos
    global grid
    grid[player_y_pos][player_x_pos - 1] = 1
    grid[player_y_pos][player_x_pos] = 0
    update_player_pos()
    print_grid()
    
def move_right():
    global player_x_pos
    global player_y_pos
    global grid
    grid[player_y_pos][player_x_pos + 1] = 1
    grid[player_y_pos][player_x_pos] = 0
    update_player_pos()
    print_grid()