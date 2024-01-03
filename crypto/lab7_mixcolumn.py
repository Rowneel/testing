def gmul(b, a):
    p = 0
    hiBitSet = 0
    for _ in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
    return p % 256

def mix_columns(state):
    for i in range(4):
        s0 = state[i]
        s1 = state[i + 4]
        s2 = state[i + 8]
        s3 = state[i + 12]

        state[i] = gmul(2, s0) ^ gmul(3, s1) ^ s2 ^ s3
        state[i + 4] = s0 ^ gmul(2, s1) ^ gmul(3, s2) ^ s3
        state[i + 8] = s0 ^ s1 ^ gmul(2, s2) ^ gmul(3, s3)
        state[i + 12] = gmul(3, s0) ^ s1 ^ s2 ^ gmul(2, s3)

def inv_mix_columns(state):
    for i in range(4):
        s0 = state[i]
        s1 = state[i + 4]
        s2 = state[i + 8]
        s3 = state[i + 12]

        state[i] = gmul(14, s0) ^ gmul(11, s1) ^ gmul(13, s2) ^ gmul(9, s3)
        state[i + 4] = gmul(9, s0) ^ gmul(14, s1) ^ gmul(11, s2) ^ gmul(13, s3)
        state[i + 8] = gmul(13, s0) ^ gmul(9, s1) ^ gmul(14, s2) ^ gmul(11, s3)
        state[i + 12] = gmul(11, s0) ^ gmul(13, s1) ^ gmul(9, s2) ^ gmul(14, s3)


state = [
    0x87, 0xf2, 0x4d, 0x97,
    0x6e, 0x4c, 0x90, 0xec,
    0x46, 0xe7, 0x4a, 0xc3,
    0xa6, 0x8c, 0xd8, 0x95
]

mix_columns(state)
print("After MixColumns:", [hex(x) for x in state])

inv_mix_columns(state)
print("After InvMixColumns:", [hex(x) for x in state])

