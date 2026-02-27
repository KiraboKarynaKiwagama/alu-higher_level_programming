#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    print(f"{number} is positive")  # ← 4 spaces (CORRECT!)
elif number == 0:
    print(f"{number} is zero")       # ← 4 spaces (CORRECT!)
else:
    print(f"{number} is negative")   # ← 4 spaces (CORRECT!)
