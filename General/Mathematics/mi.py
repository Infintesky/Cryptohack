# EXAMPLE: 7 * 8 = 56 ≡ 1 mod 11
"""
7 * d =  1 mod 11
gcd(11, 7) == 1

step 1: Find GCD
11 = 1(7) + 4
7 = 1(4) + 3
4 = 1(3) + 1

step 2: Express 1 as diff between 11 and 7
1 = 4 - 1(3)
1 = 2(4) - 1(7)
1 = 8(7) - 5(11)

step 3: apply modulo 11 on both sides
1 = 8(7) mod 11
Hence 8 is answer

"""
# FLAG: 3 * d ≡ 1 mod 13
"""
3 * d mod 13 = 1
"""


def find_inverse(g, p):
    """Given g * d ≡ 1 mod p, where g and p are given, find value of d

    Returns:
        [int]: [integer value of d or 0 if can't find any value d] 
    """
    for i in range(1000):
        if (g * i % p) == 1:
            return i

    return 0


print(find_inverse(3, 13))
