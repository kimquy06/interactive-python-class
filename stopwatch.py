# template for "Stopwatch: The Game"
# Import modules
import simplegui
# define global variables
time = 0
interval = 100

width = 200
height = 200

position_clock = [width/2, height/2]
position_score = [160, 25]

is_running = False

number_of_stop = 0
number_of_right = 0

clock = "0:00.0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute = t /600
    ten_of_second = (t/10)%60/10
    second = (t/10)%60%10
    tenth_of_second = t %10
    return str(minute) + ":" + str(ten_of_second) + str(second) + "." + str(tenth_of_second)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_running
    is_running = True
    timer.start()    
    
def stop():    
    global number_of_stop, number_of_right, is_running    
    if(is_running==True):
        number_of_stop = number_of_stop + 1
        if(clock[-1]=='0'):
            number_of_right = number_of_right + 1
    is_running = False
    timer.stop()
    
def reset():
    global time, number_of_stop, number_of_right
    time = 0        
    number_of_stop = 0
    number_of_right = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1


# define draw handler
def draw(canvas):
    global clock
    clock = format(time)  
    canvas.draw_text(clock, position_clock, 20, "White")
    score = str(number_of_right) + "/" + str(number_of_stop)
    canvas.draw_text(score, position_score, 20, "Red")
    
# create frame
frame = simplegui.create_frame("Home", width, height)

# register event handlers
frame.add_button("Start", start, 50)
frame.add_button("Stop", stop, 50)
frame.add_button("Reset", reset, 50)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()


# Please remember to review the grading rubric
