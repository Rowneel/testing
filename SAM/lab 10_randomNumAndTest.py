def mixedCongruential(n):
    x0 = int(input("Enter Seed Multiplier x0: "))
    a = int(input("Enter Constant Multiplier a: "))
    c = int(input("Enter increament c: "))
    m = int(input("Enter modulus m: "))
    Arr = []
    for i in range(n):
        x0 = (a*x0 + c) % m
        Arr.append(x0/m)
    return Arr

def KS_sampleOver50(D,N):
    if D < 1.36/(N**0.5):
        print("The random Numbers are uniformly distributed.")
    else:
        print("The random Numbers are not uniformly distributed.")

def calculate_Kolmogorov_Smirnov(Ri):
    Ri.sort()
    N = len(Ri)

    Dplus = [(i + 1) / N - Ri[i] for i in range(N)]
    Dminus = [Ri[i] - (i / N) for i in range(N)]

    DP = max(Dplus)
    DM = max(Dminus)

    D = max(DP, DM)
    
    if N > 50:
        KS_sampleOver50(D,N)
    else:
        print(f'Calculated value of D is {D}')
        print(f'If {D} is less than critical value D from table we accept that it is Uniform. Otherwise it is not uniform. For sample greater than 50 tabulated D value is 1.36/sqrt(N)')
        
def autoCorrelation(i,m,R):
    N = len(R)
    M = (N-m-i)//m
    sumation = 0
    for k in range(M+1):
        sumation = sumation + (R[(i+k*m)-1] * R[(i+(k+1)*m)-1])
    rho = (1/(M+1))*sumation - 0.25
    sigma = ((13*M+7)**0.5)/(12*(M+1))
    z = rho/sigma
    if z < 1.96:
        print(f'z calculated {z} < z tabulated 1.96. So, The numbers are independent.')
    else:
        print("The numbers are not independent")


quantity = 56
randomNum = mixedCongruential(quantity)
print(randomNum)
# for uniformity
calculate_Kolmogorov_Smirnov(randomNum)
# for independence 
autoCorrelation(2,5,randomNum)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 11, 12, 13, 14, 15, 100, 16, 17, 18, 19, 20, 200, 21, 22, 23, 24, 25, 200, 26, 27, 28, 29, 30]
# autoCorrelation(2,5,numbers)

