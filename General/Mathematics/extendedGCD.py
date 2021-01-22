def extended_gcd(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(num2 % num1, num1)
        return (gcd, v - (num2 // num1) * u, u)


gcd, u, v = extended_gcd(26513, 32321)
print("GCD =", gcd)
print("u =", u)
print("v =", v)
