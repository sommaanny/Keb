import sys
import time
import random
import user as u
import enemy as e

while(True):
    print("Chose Poketmon 1) Pikachu 2) Charmander(파이리) 3) Squirtle(꼬부기) 4) exit")
    number = int(sys.stdin.readline())
    if number == 1:
        me = u.Pikachu()
    elif number == 2:
        me = u.Charmander()
    elif number == 3:
        me = u.Squirtle()
    elif number == 4:
        break
    else:
        print("Please Enter the right number")

    print("Creating the enemy..")
    time.sleep(3)

    n = random.randint(1,3)
    if n == 1:
        enemy = e.Meowth()
    elif n == 2:
        enemy = e.Magikarp()
    else:
        enemy = e.Dragonite()
    
