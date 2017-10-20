#Ghost Game
from random import randint
print("Ghost Game")

feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = randint(1,3)
    print("Three doors ahead...")
    print("A Big Ghost behind one, which will eat you :-(")
    print("Which door do you open?")
    door = input("1, 2, or 3?")
    door_num = int(door)
    if door_num == ghost_door:
        print("GHOST!")
        feeling_brave = False
    else:    
        print("no ghost!")
        print("you enter the next room")
        score = score + 1
print("run away!")
print("game over! you scored", score)
