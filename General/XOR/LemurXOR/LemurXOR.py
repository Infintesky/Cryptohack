from PIL import Image
from pwn import xor

lemur = Image.open("lemur.png")
flag = Image.open("flag.png")

leak_bytes = xor(lemur.tobytes(), flag.tobytes())
flag_xor_lemur = Image.frombytes(
    flag.mode, flag.size, leak_bytes).save('flag_xor_lemur.png')
