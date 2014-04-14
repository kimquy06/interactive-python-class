# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# initialize global variables used in your code
num_range = 100
remain_guess = 7
secret_number = 36

# helper function to start and restart the game
def new_game():   
    global remain_guess, secret_number
    remain_guess = int(math.log(num_range, 2)) + 1
    secret_number = random.randrange(0,num_range)
    
    print ' '
    print 'New game. Range is from 0 to ' + str(num_range)    
    print 'Number of remainding guesses is ' + str(remain_guess)
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts  
    global num_range
    num_range = 100        
    new_game()
    
def range1000():
    # button that changes range to range [0,1000) and restarts    
    global num_range
    num_range = 1000    
    new_game()
    
def input_guess(guess):
    # main game logic goes here	 
    global remain_guess
    guess = int(guess)
    print ' '
    print 'Guess was ' + str(guess)
    remain_guess = remain_guess -1
    print "Number of remainding guesses is " + str(remain_guess)
    if(guess > secret_number):                        
        print "Lower!"        
    elif (guess < secret_number):
        print "Higher!"        
    else:
        print "Correct!"
        new_game()
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
# call new_game and start frame
new_game()

