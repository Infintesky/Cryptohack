import pem


certs = pem.parse_file("PEM.pem")
print(certs)
