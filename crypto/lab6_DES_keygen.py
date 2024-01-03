def apply_permutation(data, permutation_table):
    return ''.join(data[i - 1] for i in permutation_table)

def left_shift(data, amount):
    return data[amount:] + data[:amount]

Permutated_Choice1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    11,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]
Permutated_Choice2 = [
    14, 17, 11, 24,  1,  5,
    3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]


shift_amount_for_each_round = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def generate_subkeys(key):
    key_binary = format(int(key, 16), '064b')
    key_permuted = apply_permutation(key_binary, Permutated_Choice1)

    C = [key_permuted[i] for i in range(28)]
    D = [key_permuted[i] for i in range(28, 56)]

    subkeys = []
    for i in range(16):
        shift_amount = shift_amount_for_each_round[i]
        C = left_shift(C, shift_amount)
        D = left_shift(D, shift_amount)
        subkey_halves = C + D
        subkey = apply_permutation(subkey_halves, Permutated_Choice2)  
        subkeys.append(subkey)
    
    return subkeys

if __name__ == "__main__":
    des_key = "0E329232EA6D0D73"
    subkeys = generate_subkeys(des_key)

    for i, subkey in enumerate(subkeys):
        print(f"Subkey {i+1}: {subkey}")