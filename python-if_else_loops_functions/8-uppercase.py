#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line"""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32 from ASCII value
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            # Print non-lowercase characters as is
            print("{}".format(c), end="")
    print()
