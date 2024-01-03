def additive_inverse_modulo(a, m):
    # Calculate the additive inverse modulo m
    inverse = m - a

    return inverse % m

# Example usage
a = 205
m = 6

print(f"Additive inverse of {a} mod {m} is {additive_inverse_modulo(a, m)}")
