import math
 
def egcd(a,b):
    if a == 0:
        return (b,0,1)
    g,y,x = egcd(b%a,a)
    return (g,x - (b // a)*y,y)

def inverse(e,phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        print('modular inverse does not exist')
        exit(0)
    else:
        return (x % phi + phi) % phi
        
# step 1
p = 3
q = 7
 
# step 2
n = p*q
print("n =", n)
 
# step 3
phi = (p-1)*(q-1)
 
# step 4
e = 2
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
 
print("e =", e)
# step 5
k = 2

d = inverse(e,phi)
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
 
# plain text
msg = 11
print(f'Original message:{msg}')
 
# encryption
C = msg ** e
C = C % n
print(f'Encrypted message: {C}')
 
# decryption
M = pow(C, d)
M = math.fmod(M, n)
 
print(f'Decrypted message: {M}')

print(-7 % 3)