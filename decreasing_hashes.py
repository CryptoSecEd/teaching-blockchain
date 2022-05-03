#!/usr/bin/env python3

""" Find a sequence of inputs that hash to successively smaller digests
"""

from hashlib import sha256
from random import random


def gen_hash(string):
    """ Calculates a hash of a string
    """
    hasher = sha256()
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()


def main():
    """ Keep searching for strings whose hashes are lower values than
    the previous
    """
    base = "Decreasing hashes: "
    winner = base+str(random())
    lowest = gen_hash(winner)
    # This next line is generally a bad idea. It will run forever
    # (or until you press CTRL-C)
    while True:
        test = base + str(random())
        # If the hash is lower than the best so far, we update winner
        # and lowest
        if gen_hash(test) < lowest:
            winner = test
            lowest = gen_hash(test)
            print(f"{lowest} {winner}")


if __name__ == "__main__":
    main()
