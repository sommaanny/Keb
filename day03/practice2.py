#연습문제 6.5 - 6.1
list_test = [3, 2, 1, 0]
for i in list_test:
    print(i, end=' ')
print()

#연습문제 6.2
guess_me = 7
number = 1
while(True):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
    elif number > guess_me:
        print("oops")
        break
    number += 1
print()

#연습문제 6.3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me:
        print("opps")
        break
