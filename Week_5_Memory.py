# implementation of card game - Memory

import simplegui
import random

WIDTH = 50
HEIGHT = 100
turns = 0
state = 0
choices = [-1,-1]
num_list = []
exposed = []

# helper function to initialize globals
def new_game():
    global num_list, exposed, turns, state, choices
    num_list = range(0, 8)
    num_list.extend(num_list)
    random.shuffle(num_list)
    exposed = [0] * 16
    turns = 0
    state = 0
    choices=[-1,-1]
    label.set_text("Turns = " + str(turns))
      
# define event handlers
def mouseclick(pos):
    global choices, state, turns
    index = int(pos[0]/WIDTH)
    if(state == 0):
        if(exposed[index] == 0):
            if(num_list[choices[0]] != num_list[choices[1]]):
                exposed[choices[0]] = 0
                exposed[choices[1]] = 0
            exposed[index] = 1
            state = 1
            choices[0] = index
    elif state == 1:
        if(exposed[index] == 0):
            state = 0
            exposed[index] = 1
            choices[1] = index
            turns = turns + 1
            label.set_text("Moves = " + str(turns))
            if not(0 in exposed):
                print "The game ended in " + str(turns) + " moves"
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for index in range(0,len(num_list)):
        if(exposed[index] == 0):
            canvas.draw_polygon([(WIDTH*index,0), (WIDTH*(index+1), 0), (WIDTH*(index+1), 100),(WIDTH*index,100)],3,"Navy","Green")
        else:
            canvas.draw_text(str(num_list[index]),[WIDTH*index+5,HEIGHT-25],60,"White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric

http://www.codeskulptor.org/#user38_B6ZiFic03zOSl2B.py