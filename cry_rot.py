#!/usr/bin/env python3

import math

cipher = "hello"

for i in range(26):
    plane = ''
    n = 0
    for c in cipher:
        if c.isalpha():
            # convert
            cc = chr(ord(c) - i)
            # fix out of loop
            val = 'a' if c.islower() else 'A'
            cc = chr(((ord(cc)-ord(val)) % 26) + ord(val))

            plane += cc
        else:
            plane += c

    print(plane.lower())
