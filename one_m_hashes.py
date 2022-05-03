#!/usr/bin/env python3

"""Calculates 1 million sha256 hashes of random data.
Prints execution time.
"""

from hashlib import sha256
from random import randint
from time import time


def gen_hash(string):
    """Calculate a sha256 hash of a message.
    """
    hasher = sha256()
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()


def main():
    """Loop over hash calculation 1M times.
    """
    start = time()
    for count in range(0, 1000000):
        random_int = randint(1, 1000000000000)
        # gen_hash("Some random value: %d %d" % (count, random_int))
        gen_hash(f"Some random value: {count} {random_int}")
    print("Finished calculating 1 million hashes")
    print(f"Execution time: {time()-start} seconds")


if __name__ == "__main__":
    main()
