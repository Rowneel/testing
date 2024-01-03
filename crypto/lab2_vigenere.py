# Vigenere cipher
def encrypt(plaintext):
    key = input("Enter Key: ")
    key = key.upper()
    j = 0
    cypher_text = []
    for char in plaintext:
        if j >= len(key):
            j = 0
        char_pos = ord(char.upper()) - ord("A")
        key_pos = ord(key[j]) - ord("A")
        cypher_char = chr(((char_pos + key_pos) % 26) + ord("A"))
        j += 1
        cypher_text.append(cypher_char)
    print("".join(cypher_text))
    return cypher_text


def decrypt(cypher_text):
    key = input("Enter Key: ")
    key = key.upper()
    j = 0
    message = []
    for char in cypher_text:
        if j >= len(key):
            j = 0
        char_pos = ord(char.upper()) - ord("A")
        key_pos = ord(key[j]) - ord("A")
        message_char = chr(((char_pos - key_pos) % 26) + ord("A"))
        j += 1
        message.append(message_char)
    print("".join(message))
    return message


def main():
    while True:
        choice = input("Enter:\n1. Encrypt\n2. Decrypt\n3. Exit\n>>>")
        match choice:
            case "1":
                plaintext = input("Enter message: ")
                encrypt(plaintext)
            case "2":
                cypher_text = input("Enter encrypted text: ")
                decrypt(cypher_text)
            case "3":
                exit()
            case _:
                print("INVALID CHOICE!!")


if __name__ == "__main__":
    main()
