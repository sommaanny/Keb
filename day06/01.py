def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

import random

numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
try:
    pick = int(input("Input index : "))
    print("Your pick number is " , numbers[pick])
except IndexError as err:
    print(err)
    print("Please Enter number 0 to 5")
except ValueError as err:
    print(err)
    print("Please Enter only digit number")
except:
    print("Error")