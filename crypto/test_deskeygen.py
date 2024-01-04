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

shift_amount_each_round = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


def apply_permutation(binary_key,ptable):
    return "".join(binary_key[i-1] for i in ptable)


def generate_subkey(key):
    binary_key = format(int(key,16),'064b')
    permuted_key = apply_permutation(binary_key,Permutated_Choice1)
    left_half_key = permuted_key[0:28]
    right_half_key = permuted_key[28:56]
    subkeys = []
    for i in range(16):
        left_half_key = left_half_key[shift_amount_each_round[i]:] + left_half_key[:shift_amount_each_round[i]]
        right_half_key = right_half_key[shift_amount_each_round[i]:] + right_half_key[:shift_amount_each_round[i]]
        
        final_subkey = left_half_key+right_half_key
        final_subkey = apply_permutation(final_subkey,Permutated_Choice2)
        subkeys.append(final_subkey)
    return subkeys

key = "0E329232EA6D0D73"
subkeys = generate_subkey(key)
for i,subkey in enumerate(subkeys):
    print(f'Subkey {i+1}: {subkey}')
