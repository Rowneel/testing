def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print('modular inverse does not exist')
        exit(0)
    else:
        return (x % m + m) % m
    
print('Multiplicative imverse of 7 mod 11 is',modinv(7,11))