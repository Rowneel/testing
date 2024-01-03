# Ceaser cipher

def encrypt(plaintext):
    key = int(input("Enter Key: "))
    cypher_text = []
    for char in plaintext:
        if char.isupper():
            cypher_char = chr((ord(char) - ord("A") + key) % 26 + ord("A"))
        elif char.islower():
            cypher_char = chr((ord(char) - ord("a") + key) % 26 + ord("a"))
        else:
            cypher_char = char
        cypher_text.append(cypher_char)
    print("".join(cypher_text))
    return cypher_text


def decrypt(cypher_text):
    key = int(input("Enter Key: "))
    message = []
    for char in cypher_text:
        if char.isupper():
            plain_char = chr((ord(char) - ord("A") - key) % 26 + ord("A"))
        elif char.islower():
            plain_char = chr((ord(char) - ord("a") - key) % 26 + ord("a"))
        else:
            plain_char = char
        message.append(plain_char)
    print("".join(message))


def main():
    plaintext = input("Enter message: ")
    print(plaintext)
    cypher_text = encrypt(plaintext)
    decrypt(cypher_text)


if __name__ == "__main__":
    main()
