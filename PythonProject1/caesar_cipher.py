alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(text, shift):
    text_as_list = []
    encrypted_text = ''
    for char in text:
        text_as_list.append(char)
    print(text_as_list)
    for char in text_as_list:
        if char.isalpha():
            letter_key = alphabet.index(char)
            new_letter = (letter_key + shift) % 26
            new_letter = alphabet[new_letter]
            encrypted_text += new_letter
        else:
            encrypted_text += char
    return encrypted_text
def decrypt(text, shift):
    text_as_list = []
    decrypted_text = ''
    for char in text:
        text_as_list.append(char)
    print(text_as_list)
    for char in text_as_list:
        if char.isalpha():
            letter_key = alphabet.index(char)
            new_letter = (letter_key + shift) % 26
            new_letter = alphabet[new_letter]
            decrypted_text += new_letter
        else:
            decrypted_text += char
    return decrypted_text
def caesar_cypher():
    text = input('What is your plaintext/Ciphertext\n')
    key = int(input('What is the key to your cypher?\n'))
    encrypt_or_decrypt = input('Do you want to encrypt or decrypt your text (decrypt auto swaps the key)?\n')
    if 'encrypt' in encrypt_or_decrypt.lower():
        text = text.lower()
        print(encrypt(text, key))
    else:
        text = text.lower()
        key = key * - 1
        print(decrypt(text, key))
