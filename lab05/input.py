#!/usr/bin/env python3

"""This code shows an example of how to read input from the user
"""


def main():
    """Get input from the user and perform some simple operations on
    the text
    """
    text_input = input("Please type some letters: ")
    print("You have typed: " + text_input)
    print("Input in lowercase: " + text_input.lower())
    print("Input in uppercase: " + text_input.upper())
    print("Input as title: " + text_input.title())
    print("Length: " + str(len(text_input)))


# This is common in python code, and can be ignored for now
if __name__ == "__main__":
    main()
