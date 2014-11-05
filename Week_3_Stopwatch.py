# template for "Stopwatch: The Game"
import simpleguitk as simplegui

# define global variables
time = 0
interval = 100
total_stops = 0
success_stops = 0
A = B = C = D = 0
stopped = True


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


# define event handlers for buttons; "Start", "stop", "Reset"
def start():
    global time, stopped
    stopped = False
    timer.start()


def stop():
    global total_stops, success_stops, stopped
    if not stopped:
        if time % 10 == 0 and time != 0:
            success_stops += 1
            total_stops += 1
        elif time != 0:
            total_stops += 1
    stopped = True
    timer.stop()


def reset():
    global time, success_stops, total_stops, stopped
    time = 0
    total_stops = 0
    success_stops = 0
    stopped = True
    timer.stop()


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1


# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), (80, 125), 42, "white")
    canvas.draw_text(str(success_stops) + '/' + str(total_stops), (150, 50), 24, "Red")


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
# http://www.codeskulptor.org/#user38_7bD4fRnD5I_0.py