def rail_fence_cipher(text, rails):
    mat = [["\n"] * len(text) for _ in range(rails)]
    row = 0
    col = 0
    cypher_text = []
    direction = bool
    for char in text:

        mat[row][col] = char
        col += 1

        if row == 0:
            direction = True
        elif row == rails - 1:
            direction = False

        if direction:
            row += 1
        else:
            row -= 1

    for i in range(rails):
        for j in range(len(text)):
            if mat[i][j] != "\n":
                cypher_text.append(mat[i][j])
    return "".join(cypher_text)


def rail_fence_decipher(text, rails):
    mat = [["\n"] * len(text) for _ in range(rails)]
    row = 0
    col = 0
    plain_text = []
    direction = bool
    for _ in text:
        if row == 0:
            direction = True
        elif row == rails - 1:
            direction = False

        mat[row][col] = "x"
        col += 1

        if direction:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if (mat[i][j] == "x") and (index < len(text)):
                mat[i][j] = text[index]
                index += 1
    row = 0
    col = 0
    for i in range(len(text)):

        # check the direction of flow
        if row == 0:
            direction = True
        elif row == rails - 1:
            direction = False

        # place the marker
        if mat[row][col] != "x":
            plain_text.append(mat[row][col])
            col += 1

        # find the next row using
        # direction flag
        if direction:
            row += 1
        else:
            row -= 1
    return "".join(plain_text)


def main():
    text = input("Enter the input string: ")
    rails = int(input("Enter rails:"))
    # Ciphering
    encrypted_text = rail_fence_cipher(text, rails)
    print("Cipher text after applying rail fence:")
    print(encrypted_text)

    # Deciphering
    encrypted_message = input("Enter encrypted text: ")
    print("Text after decryption:")
    print(rail_fence_decipher(encrypted_message, rails))


if __name__ == "__main__":
    main()
