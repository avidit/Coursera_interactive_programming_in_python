# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random

import simpleguitk as simplegui


# initialize global variables used in your code
num_range = 101
secret_num = 0
guesses_left = 0


# helper function to start and restart the game
def new_game():
    global num_range
    global secret_num
    global guesses_left

    secret_num = random.randrange(0, num_range)
    print secret_num

    if num_range == 101:
        guesses_left = 7
    elif num_range == 1001:
        guesses_left = 10

    print "New game. The range is from 0 to", num_range - 1
    print "Number of remaining guesses is ", guesses_left, "\n"


# define event handlers for control panel
def range100():
    global num_range
    num_range = 100  # button that changes range to range [0,100) and restarts
    new_game()


def range1000():
    global num_range
    num_range = 1000  # button that changes range to range [0,1000) and restarts
    new_game()


def input_guess(guess):
    # main game logic goes here	
    global guesses_left, secret_num

    print "You guessed: ", guess
    guesses_left -= 1
    if int(guess) == secret_num:
        print "Your guess is correct! Congratulations!\n"
        new_game()
        return
    elif guesses_left > 0:
        print "The number of remaining guesses is ", guesses_left
        if int(guess) > secret_num:
            print "Try Lower!"
        else:
            print "Try Higher!"
    else:
        print "Game over. You couldn't guess the correct number"
        new_game()
        return

# create frame
f = simplegui.create_frame("Game: Guess the number!", 200, 200)
f.set_canvas_background('Navy')

# register event handlers for control elements
f.add_button("Range is (0, 100)", range100, 150)
f.add_button("Range is (0, 1000)", range1000, 150)
f.add_input("Enter your guess", input_guess, 150)

# call new_game and start frame
new_game()
f.start()

# always remember to check your completed program against the grading rubric