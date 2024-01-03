def gcd(a, b):
	if a == 0:
		return b

	return gcd(b % a, a)

def primitive_check(g, p):
    L = []
    for i in range(1, p):
        L.append(pow(g, i) % p)
    # print(L)
    for i in L:
        if L.count(i) > 1:
            return False
    return True

def relative_prime(a,b):
    return gcd(a,b) == 1

def main():
    a = int(input("Enter num a: "))
    b = int(input("Enter num b: "))
    print(f"GCD of {a} and {b} is {gcd(a,b)}")
    # print(f"Is {a} and {b} relatively prime? {relative_prime(a,b)}")

def main1():
    x = int(input("Enter a number: "))
    y = int(input("Enter prime number: "))
    print(f"Is {x} primitive root of {y}? {primitive_check(x,y)}")

if __name__ == "__main__":
	main()