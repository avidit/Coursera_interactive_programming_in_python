# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
interval = 100
total_stops = 0
succes_stops = 0
A = B = C = D = 0
stop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
    D = t % 10
    C = (t / 10) % 10
    B = (t / 100) % 6
    A = (t / 600) % 10
    msg = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return msg

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global time, stop
    stop = False
    timer.start()

def stop():
    global total_stops, succes_stops, stop
    if stop == False :
        if time % 10 == 0 and time != 0 :
            succes_stops += 1
            total_stops += 1
        elif time != 0 :
            total_stops += 1
    stop = True
    timer.stop()

def reset():
    global time, succes_stops, total_stops
    time = 0
    total_stops = 0
    succes_stops = 0
    stop = True
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), (80, 125), 42, "white")
    canvas.draw_text(str(succes_stops) + '/' + str(total_stops), (150,50), 24, "Red")

    
# create frame
frame = simplegui.create_frame("Timer", 200, 200)


# register event handler
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
reset()

# Please remember to review the grading rubric
#http://www.codeskulptor.org/#user38_7bD4fRnD5I_0.py