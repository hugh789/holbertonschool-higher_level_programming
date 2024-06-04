#!/usr/bin/python3


def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz", end='')  # Remove extra space
        elif num % 3 == 0:
            print("Fizz", end='')  # Remove extra space
        elif num % 5 == 0:
            print("Buzz", end='')  # Remove extra space
        else:
            print(num, end=' ')  # Use f-string or direct formatting

