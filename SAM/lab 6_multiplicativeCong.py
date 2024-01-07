def multiplicativeCongruential(n):
    x0 = int(input("Enter Seed Multiplier x0: "))
    a = int(input("Enter Constant Multiplier a: "))
    m = int(input("Enter modulus m: "))
    Arr = []
    for i in range(n):
        x0 = (a*x0) % m
        Arr.append(x0)
    return Arr
    
def main():
    n = int(input("How many random numbers do you need? "))
    print("The random numbers are: ", multiplicativeCongruential(n))
    
if __name__ == "__main__":
    main()