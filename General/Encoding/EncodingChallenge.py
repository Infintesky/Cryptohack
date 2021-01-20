from pwn import *  # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
from binascii import unhexlify


conn = remote('socket.cryptohack.org', 13377, level='debug')


for i in range(0, 101):
    received = json_recv()
    if "flag" in received:
        print("\n[*] FLAG: {}".format(received["flag"]))
        break

    word = received["encoded"]
    encoding = received["type"]

    if encoding == "base64":
        decoded = base64.b64decode(word).decode('utf8').replace("'", '"')
    elif encoding == "hex":
        decoded = (unhexlify(word)).decode('utf8').replace("'", '"')
    elif encoding == "rot13":
        decoded = codecs.decode(word, 'rot_13')
    elif encoding == "bigint":
        decoded = unhexlify(word.replace("0x", "")).decode(
            'utf8').replace("'", '"')
    elif encoding == "utf-8":
        decoded = "".join([chr(b) for b in word])

    to_send = {
        "decoded": decoded
    }

    conn.sendline(json.dumps(to_send).encode())
