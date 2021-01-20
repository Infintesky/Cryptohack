#!/usr/bin/env python3

from pwn import *
import json

HOST = "socket.cryptohack.org"
PORT = 11112

request = {
    "buy": "flag"
}

conn = remote(HOST,PORT)

json_obj = json.dumps(request).encode()

print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
conn.sendline(json_obj)
conn.interactive()

