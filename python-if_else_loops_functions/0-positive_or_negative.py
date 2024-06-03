#!/usr/bin/python3
"""program will assign a random signed number to the variable 
number each time it is executed"""

import random
number = random.randint(-10, 10)

if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
