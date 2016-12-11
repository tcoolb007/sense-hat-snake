import sense_hat
import sys
from time import sleep
from random import randint

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
    global x
    global y
    x = path[0][0]
    y = path[0][1]
    

    if is_snake():
        quit_game()

    if direct == 0:
        x += 1
    elif direct == 1:
        y += 1 
    elif direct == 2:
        x -= 1
    else:
        y -= 1

    if is_wall():
        quit_game()
    
    path.insert(0,[x,y])
    draw_snake()
    check_food()

def is_wall():
    if x > 7 or x < 0 or y > 7 or y < 0:
        return True
    else:
        return False

def is_snake():
    for px, py in path[1:length - 1]:
        if x == px and y == py:
            return True

def draw_snake():
    sense.clear() 
    for i in range(0, length): 
        sense.set_pixel(path[i][0],path[i][1], w)

def quit_game():
    sense.set_pixels(game_over)
    running = False
<<<<<<< HEAD
    print("\nThanks for playing!")
=======
>>>>>>> fc4d8a8781b45280a88c268d79c49e5e28fad0d1
    sleep(10)
    sense.clear()
    sys.exit()

def check_food():
    global length
    if path[0][0] == food_x and path[0][1] == food_y:
        length += 1
        assign_food()
    sense.set_pixel(food_x, food_y, r)
             
def assign_food():
    snake = path[0:length - 1]
    global food_x
    global food_y

    deciding = True

    while deciding:
        food_x = randint(0,7)
        food_y = randint(0,7)

        for i in range(0, length - 1):
            if snake[i][0] == food_x and snake[i][1] == food_y:
                break
        else:
            deciding = False

assign_food()
sense.set_pixel(food_x, food_y, r)
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
    sleep(0.5)

