
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9954953
#    Student name: Lucas Wickham
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BUILDING BLOCKS
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "stack_blocks".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a pile of building blocks
#  whose arrangement is determined by data stored in a list which
#  specifies the blocks' locations.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

block_size = 250 # pixels
top_and_bottom_border = 75 # pixels
left_and_right_border = 150 # pixels
canvas_width = (block_size + left_and_right_border) * 2
canvas_height = (block_size + top_and_bottom_border) * 2

#
#--------------------------------------------------------------------#



#-----Functions for Managing the Canvas------------------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Set the coordinate system so that location (0, 0) is centred on
    # the point where the blocks will be stacked
    setworldcoordinates(-canvas_width / 2, -top_and_bottom_border,
                        canvas_width / 2, canvas_height - top_and_bottom_border)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 50 # pixels
    penup()
    goto(-(canvas_width / 2 + overlap), -(top_and_bottom_border + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(top_and_bottom_border + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(top_and_bottom_border + overlap)
    end_fill()
    penup()

    # Draw a friendly sun peeking into the image
    goto(-canvas_width / 2, block_size * 2)
    color('yellow')
    dot(250)

    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)
    

# As a debugging aid, mark the coordinates of the centres and corners
# of the places where the blocks will appear
def mark_coords(show_corners = False, show_centres = False):

    # Go to each coordinate, draw a dot and print the coordinate, in the given colour
    def draw_each_coordinate(colour):
        color(colour)
        for x_coord, y_coord in coordinates:
            goto(x_coord, y_coord)
            dot(4)
            write(' ' + str(x_coord) + ', ' + str(y_coord), font = ('Arial', 12, 'normal'))

    # Don't draw lines between the coordinates
    penup()

    # The list of coordinates to display
    coordinates = []

    # Only mark the corners if the corresponding argument is True
    if show_corners:
        coordinates = [[-block_size, block_size * 2], [0, block_size * 2], [block_size, block_size * 2],
                       [-block_size, block_size], [0, block_size], [block_size, block_size],
                       [-block_size, 0], [0, 0], [block_size, 0]]
        draw_each_coordinate('dark blue')

    # Only mark the centres if the corresponding argument is True
    if show_centres:
        coordinates = [[-block_size / 2, block_size / 2], [block_size / 2, block_size / 2],
                       [-block_size / 2, block_size + block_size / 2], [block_size / 2, block_size + block_size / 2]]
        draw_each_coordinate('red')

    # Put the cursor back how it was
    color('black')
    home()


# End the program by hiding the cursor and releasing the window
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# the building blocks:
#
# 1. The name of the block, from 'Block A' to 'Block D'
# 2. The place to put the block, either 'Top left', 'Top right',
#    'Bottom left' or 'Bottom right'
# 3. The block's orientation, meaning the direction in which the top
#    of the block is pointing, either 'Up', 'Down', 'Left' or 'Right'
# 4. An optional mystery value, 'X' or 'O', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all four blocks.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#

# The following data set doesn't require drawing any blocks
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

arrangement_00 = []

# Each of the following data sets specifies drawing just one block
# in an upright orientation.  You may find them useful when
# creating your individual pieces.

arrangement_01 = [['Block A', 'Bottom left', 'Up', 'O']]
arrangement_02 = [['Block B', 'Bottom right', 'Up', 'O']]
arrangement_03 = [['Block C', 'Bottom left', 'Up', 'O']]
arrangement_04 = [['Block D', 'Bottom right', 'Up', 'O']]

# Each of the following data sets specifies drawing just one block
# in non-upright orientations.  You may find them useful when
# ensuring that you can draw all the blocks facing in different
# directions.

arrangement_10 = [['Block A', 'Bottom left', 'Down', 'O']]
arrangement_11 = [['Block A', 'Bottom right', 'Left', 'O']]
arrangement_12 = [['Block A', 'Bottom left', 'Right', 'O']]

arrangement_13 = [['Block B', 'Bottom left', 'Down', 'O']]
arrangement_14 = [['Block B', 'Bottom right', 'Left', 'O']]
arrangement_15 = [['Block B', 'Bottom left', 'Right', 'O']]

arrangement_16 = [['Block C', 'Bottom left', 'Down', 'O']]
arrangement_17 = [['Block C', 'Bottom right', 'Left', 'O']]
arrangement_18 = [['Block C', 'Bottom left', 'Right', 'O']]

arrangement_19 = [['Block D', 'Bottom left', 'Down', 'O']]
arrangement_20 = [['Block D', 'Bottom right', 'Left', 'O']]
arrangement_21 = [['Block D', 'Bottom left', 'Right', 'O']]

# The following data sets all stack various numbers of
# blocks in various orientations

arrangement_30 = [['Block C', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Top right', 'Up', 'O']]
arrangement_31 = [['Block A', 'Bottom left', 'Up', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O']]

arrangement_32 = [['Block B', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Bottom left', 'Up', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]
arrangement_33 = [['Block B', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O']]
arrangement_34 = [['Block B', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Top left', 'Up', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

arrangement_40 = [['Block C', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top right', 'Right', 'O']]
arrangement_41 = [['Block A', 'Bottom left', 'Down', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O']]

arrangement_42 = [['Block B', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'O']]
arrangement_43 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block A', 'Top left', 'Right', 'O']]
arrangement_44 = [['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block A', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

arrangement_50 = [['Block B', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'X']]
arrangement_51 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block A', 'Top left', 'Right', 'X']]
arrangement_52 = [['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block A', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'X']]

arrangement_60 = [['Block B', 'Bottom right', 'Left', 'X'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'O']]
arrangement_61 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'X'],
                  ['Block A', 'Top left', 'Right', 'O']]
arrangement_62 = [['Block B', 'Bottom left', 'Down', 'X'],
                  ['Block A', 'Bottom right', 'Left', 'X'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

# The following arrangements create your complete image, but
# oriented the wrong way

arrangement_80 = [['Block C', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top right', 'Left', 'X'],
                  ['Block A', 'Bottom left', 'Left', 'O'],
                  ['Block B', 'Top left', 'Left', 'O']]

arrangement_81 = [['Block B', 'Bottom right', 'Right', 'X'],
                  ['Block D', 'Bottom left', 'Right', 'X'],
                  ['Block A', 'Top right', 'Right', 'O'],
                  ['Block C', 'Top left', 'Right', 'O']]

arrangement_89 = [['Block A', 'Bottom right', 'Down', 'O'],
                  ['Block C', 'Top right', 'Down', 'O'],
                  ['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block D', 'Top left', 'Down', 'O']]

# The following arrangements should create your complete image
# (but with the blocks stacked in a different order each time)

arrangement_90 = [['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'X'],
                  ['Block A', 'Top left', 'Up', 'O']]

arrangement_91 = [['Block D', 'Bottom right', 'Up', 'X'],
                  ['Block C', 'Bottom left', 'Up', 'X'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]

arrangement_92 = [['Block D', 'Bottom right', 'Up', 'X'],
                  ['Block B', 'Top right', 'Up', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O']]

arrangement_99 = [['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#

# Draw background for a block
def block_background():
    seth(0)
    fd(125)
    rt(90)
    pd()
    fillcolor('light blue')
    fill(True)
    fd(125)
    rt(90)
    fd(250)
    rt(90)
    fd(250)
    rt(90)
    fd(250)
    rt(90)
    fd(125)
    fill(False)
    pu()
    rt(90)
    fd(125)
    rt(180)

# Draw border for a block
def block_border(location):
    if location == 'Bottom left':
        goto(-125, 125)
            
    elif location == 'Bottom right':
        goto(125, 125)
                
    elif location == 'Top left':
        if bottom_l_gone == True:
            goto(-125, 125)
        else:
            goto(-125, 375)
                
    elif location == 'Top right':
        if bottom_r_gone == True:
            goto(125, 125)
        else:
            goto(125, 375)
            
    seth(0)
    fd(125)
    rt(90)
    width(2)
    pd()
    fd(125)
    rt(90)
    fd(250)
    rt(90)
    fd(250)
    rt(90)
    fd(250)
    rt(90)
    fd(125)
    pu()
    width(1)
    rt(90)
    fd(125)
    rt(180)

# Tracks if blocks in the bottom left or right are gone
global bottom_l_gone
global bottom_r_gone
bottom_l_gone = False
bottom_r_gone = False

# Draw the stack of blocks as per the provided data set
def stack_blocks(arrangement):
    
##    bottom_l_gone = False
##    bottom_r_gone = False
    colormode(255) # sets turle RGB color mode to 225
    
    for block in arrangement:
        # Check if block is missing
        if block[3] == 'O':
            # Positions blocks
            if block[1] == 'Bottom left':
                goto(-125, 125)
                block_background()
            
            elif block[1] == 'Bottom right':
                goto(125, 125)
                block_background()
                
            elif block[1] == 'Top left':
                if bottom_l_gone == True:
                    goto(-125, 125)
                    block_background()
                else:
                    goto(-125, 375)
                    block_background()
                
            elif block[1] == 'Top right':
                if bottom_r_gone == True:
                    goto(125, 125)
                    block_background()
                else:
                    goto(125, 375)
                    block_background()
                
                
            # Orients blocks
            if block[2] == 'Up':
                seth(90)

            elif block[2] == 'Down':
                seth(270)

            elif block[2] == 'Left':
                seth(180)

            elif block[2] == 'Right':
                seth(0)
                
                
            # Draws block
            if block[0] == 'Block A':
                #write('A') # used to test postion
                fd(125)
                lt(90)
                fd(1)
                pd()
                fillcolor((190, 32, 38))
                fill(True)
                lt(127)
                fd(210)
                rt(37)
                fd(83)
                rt(90)
                fd(75)
                rt(78)
                fd(260)
                fill(False)
                
                lt(180)
                pu()
                fd(130)
                pd()
                fillcolor((237, 36, 36))
                fill(True)
                rt(143)
                fd(120)
                lt(152)
                fd(220)
                lt(69)
                fd(38)
                fill(False)
                pu()
                
            elif block[0] == 'Block B':
                #write('B') # used to test position
                lt(90)
                fd(125)
                lt(90)
                fd(42)
                pd()
                fillcolor((190, 32, 38))
                fill(True)
                fd(83)
                lt(90)
                fd(64)
                lt(128)
                fd(108)
                fill(False)
                pu()

                lt(180)
                fd(108)
                lt(52)
                pd()
                fillcolor((191, 32, 38))
                fill(True)
                fd(61)
                lt(90)
                fd(65)
                lt(130)
                fd(90)
                fill(False)
                pu()

                lt(180)
                fd(90)
                rt(130)
                pd()
                fillcolor((237, 29, 36))
                fill(True)
                fd(65)
                lt(93)
                fd(100)
                lt(146)
                fd(118)
                fill(False)
                pu()
                
            elif block[0] == 'Block C':
                #write('C') # used to test position
                lt(180)
                fd(125)
                rt(90)
                fd(125)
                rt(155)
                pd()
                fillcolor((236, 31, 36))
                fill(True)
                fd(230)
                lt(77)
                fd(68)
                lt(118)
                fd(255)
                fill(False)
                pu()

                lt(180)
                fd(230)
                lt(71)
                pd()
                fillcolor((237, 36, 36))
                fill(True)
                fd(109)
                rt(111)
                fd(42)
                rt(79)
                fd(87)
                fill(False)
                pu()

                lt(180)
                fd(87)
                rt(101)
                pd()
                fillcolor((190, 32, 38))
                fill(True)
                fd(72)
                rt(90)
                fd(133)
                rt(65)
                fd(47)
                fill(False)
                pu()
                
            elif block[0] == 'Block D':
                #write('D') # used to test position
                fd(46)
                lt(37)
                pd()
                fillcolor((191, 32, 38))
                fill(True)
                fd(100)
                rt(127)
                fd(60)
                rt(90)
                fd(80)
                fill(False)

                fillcolor((190, 32, 38))
                fill(True)
                rt(142)
                fd(100)
                lt(52)
                fd(63)
                lt(90)
                fd(131)
                lt(112)
                fd(137)
                fill(False)
                pu()

            block_border(block[1])

        elif block[3] == 'X':
            if block[1] == 'Bottom left':
                global bottom_l_gone
                bottom_l_gone = True
            
            elif block[1] == 'Bottom right':
                global bottom_r_gone
                bottom_r_gone = True

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
#speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by stacking your blocks correctly
title('Origami Bird')

# Display the corner and centre coordinates of the places where
# the blocks must be placed
# ***** If you don't want to display the coordinates change the
# ***** arguments below to False
mark_coords(False, False)

### Call the student's function to display the stack of blocks
### ***** Change the argument to this function to test your
### ***** code with different data sets
stack_blocks(arrangement_99)

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

