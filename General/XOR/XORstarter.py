data = "label"
flag = ''

for char in data:
    flag += chr(ord(char) ^ 13)

print('crypto{{{}}}'.format(flag))
