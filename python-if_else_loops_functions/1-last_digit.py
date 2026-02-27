#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last digit, handling negative numbers correctly
if number < 0:
    last_digit = abs(number) % 10 * -1
else:
    last_digit = number % 10
# Print the required output
print(f"Last digit of {number} is {last_digit}", end="")
# Check conditions for the last digit
if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print(" and is 0")
else:  # last digit is less than 6 and not 0
    print(" and is less than 6 and not 0")
