#!/usr/bin/env python3

"""Calculates a hash of a string using a function.
"""

from hashlib import sha256


def gen_hash(string):
    """ Calculates a hash of a string
    """
    hasher = sha256()
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()


def main():
    """This is the main body of the code (make changes here to change
    what the code does)
    """
    text = "This is a fantastic line of text! Wow!"
    print(gen_hash(text))


if __name__ == "__main__":
    main()
