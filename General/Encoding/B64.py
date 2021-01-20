import base64

FLAG_HEX = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

flag_bytes = bytes.fromhex(FLAG_HEX)

flag_decoded = base64.b64encode(flag_bytes)

print(flag_decoded)
