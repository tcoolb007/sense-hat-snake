import sense_hat
import sys
from time import sleep

sense = sense_hat.SenseHat()

path = [[0,3],[1,3],[2,3]]
length = 3
# 0 is right, 1 is down, 2 is left, 3 is up

direct = 0

w = (255, 255, 255)
r = (255,   0,   0)
e = (  0,   0,   0)

game_over = [
w,w,w,w,w,w,w,w,
e,e,e,e,e,e,e,e,
w,w,w,w,w,w,w,w,
e,e,e,e,e,e,e,e,
w,w,w,w,w,w,w,w,
e,e,e,e,e,e,e,e,
w,w,w,w,w,w,w,w,
e,e,e,e,e,e,e,e
]

def update_snake():
    x = path[0][0]
    y = path[0][1]
    if isValid():
        if direct == 0:
            x += 1
        elif direct == 1:
            y += 1 
        elif direct == 2:
            x -= 1
        else:
            y -=  1
    else:
        quit_game()
    
    path.insert(0,[x,y])
    draw_snake()

def isValid():
    x = path[0][0]
    y = path[0][1]

    if direct == 3 and y == 0:
        return False
    elif direct == 2 and x == 0:
        return False
    elif direct == 1 and y == 7:
        return False
    elif direct == 0 and x == 7:
        return False
    else:
        return True

def draw_snake():
    sense.clear() 
    for i in range(0, length): 
        sense.set_pixel(path[i][0],path[i][1], w)

def quit_game():
    sense.set_pixels(game_over)
    running = False
    sleep(10)
    print("\nThanks for playing!")
    sense.clear()
    sys.exit()

running = True

while running == True: 
    for e in sense.stick.get_events(): 
        if e.action == sense_hat.ACTION_PRESSED:
            if e.direction == sense_hat.DIRECTION_UP and direct != 1:
                direct = 3
            elif e.direction == sense_hat.DIRECTION_DOWN and direct != 3:
                direct = 1
            elif e.direction == sense_hat.DIRECTION_LEFT and direct != 0:
                direct = 2
            elif e.direction == sense_hat.DIRECTION_RIGHT and direct != 2:
                direct = 0
    update_snake()
    sleep(1)

