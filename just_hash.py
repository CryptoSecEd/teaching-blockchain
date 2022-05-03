#!/usr/bin/env python3

"""Just hashes a static string
"""

from hashlib import sha256


hasher = sha256()
hasher.update("This is a great string!".encode('utf-8'))
print(hasher.hexdigest())
