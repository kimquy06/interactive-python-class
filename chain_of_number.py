# Mystery computation in Python
# Takes input n and computes output named result
# divide by two if the number is even or
# multiply by 3 and add 1 if the number is odd.
# 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
import simplegui

# global state

n = 1
# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n
    
def get_next(current):
    """???  Part of mystery computation."""
    if(current%2==0):
        return current/2
    else:
        return current*3 + 1

# timer callback

def update():
    """???  Part of mystery computation."""
    global n
    if(n>1):
        print str(n)
        n = get_next(n)
    else:
        print str(n)
        timer.stop()
    

# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(23)
timer.start()