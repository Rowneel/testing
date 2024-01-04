def prepare_text(text):
    text = text.lower().replace(" ","").replace("j","i")
    return text

def make_key_square(key):
    key = prepare_text(key)
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key_square = list(key)
    
    for letter in alphabet:
        if letter not in key_square:
            key_square.append(letter)
    key_square = [key_square[i:i+5] for i in range(0,25,5)]
    
    return key_square

def find_letter_location(key_square,letter):
    for i in range(5):
        for j in range(5):
            if key_square[i][j] == letter:
                return (i,j)
            
def encrypt(plaintext,key):
    plaintext = prepare_text(plaintext)
    if len(plaintext) % 2 == 1:
        plaintext += 'x'   
    digraphs = [plaintext[i:i+2] for i in range(0,len(plaintext),2)]
    key_square = make_key_square(key)
    for row in key_square:
        print(" ".join(row))
    ciphertext = []
    for digraph in digraphs:
        a,b = digraph
        if a == b:
            b = 'z'
        row_a,col_a = find_letter_location(key_square,a)
        row_b,col_b = find_letter_location(key_square,b)
        if row_a == row_b:
            ciphertext += key_square[row_a][(col_a+1) % 5] + key_square[row_b][(col_b+1) % 5]
        if col_a == col_b:
            ciphertext += key_square[(row_a+1)%5][col_a] + key_square[(row_b+1)%5][col_b]
        else:
            ciphertext += key_square[row_a][col_b] + key_square[row_b][col_a]
    return "".join(ciphertext)

def decrypt(cyphertext,key):
    digraphs = [cyphertext[i:i+2] for i in range(0,len(cyphertext),2)]
    key_square = make_key_square(key)
    plaintext = []
    for digraph in digraphs:
        a,b = digraph
        row_a,col_a = find_letter_location(key_square,a)
        row_b,col_b = find_letter_location(key_square,b)

        if row_a == row_b:
            plaintext += key_square[row_a][(col_a-1) % 5] + key_square[row_b][(col_b-1) % 5]
        if col_a == col_b:
            plaintext += key_square[(row_a-1)%5][col_a] + key_square[(row_b-1)%5][col_b]
        else:
            plaintext += key_square[row_a][col_b] + key_square[row_b][col_a]
    return "".join(plaintext)

def main():
    key = input("Enter the key: ")
    plaintext = input("Enter the plain text: ")
    ciphertext = encrypt(plaintext,key)
    print("Cipher Text:", ciphertext)
    decrypted_text = decrypt(ciphertext,key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
