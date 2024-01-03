import random 

def miillerTest(m, n):
	a = random.randint(2, n - 2)
	x = pow(a,m) % n

	if (x == 1 or x == n - 1):
		return True

	while (m != n - 1):
		x = (x * x) % n
		m *= 2
		if (x == 1):
			return False
		if (x == n - 1):
			return True
	return False

def isPrime(n, k):
	if (n <= 1 or n == 4):
		return False
	if (n <= 3):
		return True

	# Find m such that n = 2^d * m + 1 for some m >= 1
	m = n - 1
	while (m % 2 == 0):
		m //= 2

	for _ in range(k):
		if (miillerTest(m, n) == False):
			return False
	return True

# Driver Code
# Number of iterations
k = 4
p = int(input("Enter a number: "))
print(f"Is {p} Prime? {isPrime(p, k)}")


