#!/usr/bin/env python3

import math

cipher = "OMMGYL{4jikqs sgrbll}"
key = "1234567"
key *= math.ceil(len(cipher) / len(key))

plane = ''
n = 0
for c in cipher:
    if c.isalpha():
        # convert
        cc = chr(ord(c) - int(key[n]))
        # fix out of loop
        val = 'a' if cc.islower() else 'A'
        cc = chr(((ord(cc)-ord(val)) % 26) + ord(val))

        plane += cc
        n += 1
    else:
        plane += c

print(plane)
