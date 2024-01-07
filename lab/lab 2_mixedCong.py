def mixedCongruential(n):
    x0 = int(input("Enter Seed Multiplier x0: "))
    a = int(input("Enter Constant Multiplier a: "))
    c = int(input("Enter increament c: "))
    m = int(input("Enter modulus m: "))
    Arr = []
    for i in range(n):
        x0 = (a*x0 + c) % m
        Arr.append(x0)
    return Arr
    
def main():
    n = int(input("How many random numbers do you need? "))
    print("The random numbers are: ", mixedCongruential(n))
    
if __name__ == "__main__":
    main()