# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    number = -1
    if(name =='rock'):
        number = 0
    elif(name =='Spock'):
        number = 1
    elif(name == 'paper'):
        number = 2
    elif(name == 'lizard'):
        number = 3
    elif(name == 'scissors'):
        number = 4
    else:
        print 'Your choice must be rock or Spock or paper or lizard or scissors'
    return number


def number_to_name(number):
    name = ' '
    if(number==0):
        name = 'rock'
    elif(number == 1):
        name = 'Spock'
    elif(number == 2):
        name = 'paper'
    elif(number == 3):
        name = 'lizard'
    elif(number == 4):
        name = 'scissors'
    else:
        print 'Out of range 0-4'
    return name

def rpsls(player_choice):     
    
    # print a blank line to separate consecutive games
    print ' '

    # print out the message for the player's choice    
    print 'Player chooses ' + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice

    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number)%5
    #if(diff<0):
        #diff = diff + 5   

    # use if/elif/else to determine winner, print winner message
    if(diff==1 or diff ==2):
        print 'Computer wins!'
    elif(diff==3 or diff ==4):
        print 'Player wins!'
    else:
        print 'Player and computer tie!'
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


