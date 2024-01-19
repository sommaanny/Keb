import sys
import time
import random
import user as u
import enemy as e

me = None
enemy = None
flag = 0
while(True):
    print("Chose Poketmon 1) Pikachu 2) Charmander(파이리) 3) Squirtle(꼬부기) 4) exit")
    number = int(sys.stdin.readline())
    if number == 1:
        me = u.Pikachu()
        print()
        break
    elif number == 2:
        me = u.Charmander()
        print()
        break
    elif number == 3:
        me = u.Squirtle()
        print()
        break
    elif number == 4:
        flag = 1
        break
    else:
        print("Please Enter the right number")
        print()

while(True and flag == 0):
    print("Creating the enemy..")
    time.sleep(3)
    print()
    n = random.randint(1,3)
    if n == 1:
        enemy = e.Meowth()
        print()
    elif n == 2:
        enemy = e.Magikarp()
        print()
    else:
        enemy = e.Dragonite()
        print()
    
    while(me.getHP() > 0 and enemy.getHP() > 0):
        print("Chose number 1)basic attack 2)skill attack 3)run 4) exit")
        num = int(sys.stdin.readline())
        print()
        if num == 1:
            enemy.damage(me.getBasicDamage())
            print(f"Deals {me.getBasicDamage()} damage to the enemy.")
            print(f"Enemy HP is : {enemy.getHP()}")
        elif num == 2:
            enemy.damage(me.skill())
            print(f"Enemy HP is : {enemy.getHP()}")
        elif num == 3:
            break
        else:
            print("Please Enter the right number")
            print()
        
        if enemy.getHP() > 0:
            print()
            print("Enemy Turn")
            print()
        else:
            break
        time.sleep(2)
        
        random_attack = random.randint(1,2)
        if n == 1 or random_attack == 1:
            me.damage(enemy.getBasicDamage())
            print(f"You took {enemy.getBasicDamage()} damage.")
            print(f"Your HP is : {me.getHP()}")
        else:
            me.damage(enemy.skill())
        print()
        time.sleep(2)
    
    if me.getHP() <= 0:
        print("You Lose")
    else:
        print("You win!")
    break