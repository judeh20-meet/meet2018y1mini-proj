# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name: Judeh A
Date:
"""
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for number_steps  in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position Lwith snake.pos()[0]
    y_pos=snake.pos()[1]
    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)

    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp1 = snake.stamp()
    stamp_list.append(stamp1)



###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

##2. Make functions down(), left(), and right() that change direction
#####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    print('You pressed the down key!')

def left():
    global direction
    direction=LEFT
    print('You pressed the left key!')

def right():
    global direction
    direction=RIGHT
    print('You pressed the right key!')

turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
##3. Do the same for the other arrow keys
#####WRITE YOUR CODE HERE!!

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()



    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    
   
    

#    #Stamp new element and append new stamp in list
#    #Remember: The snake position changed - update my_pos()
#
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
#    ######## SPECIAL PLACE - Remember it for Part 5
#    #pop zeroth element in pos_list to get rid of last the last 
#    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()    
    


###################################################################
#           PART 3
####################################################################
#
##Go to the top of your file, and after the line that says direction = UP,  write:
#
#UP_EDGE = 250
#DOWN_EDGE = -250
#RIGHT_EDGE = 400
#LEFT_EDGE = -400
#
#
##Now go add code to the end of your  move_snake() function
#
#def move_snake():
#
#    . . .
#

#    #Add new lines to the end of the function
#    #Grab position of snake
#    new_pos = snake.pos()
#    new_x_pos = new_pos[0]
#    new_y_pos = new_pos[1]
#
## The next three lines check if the snake is hitting the 
## right edge.
#if new_x_pos >= RIGHT_EDGE:
#print(“You hit the right edge! Game over!”)
#quit()
#
#     # You should write code to check for the left, top, and bottom edges.
#    #####WRITE YOUR CODE HERE
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food.stamp()
    food_stamps.append(this_food_pos)
    


