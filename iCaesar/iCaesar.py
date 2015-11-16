__author__ = 'Code Hobbits'

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(plaintext, key):
    ciphertext = ""
    counter = 0
    while counter < len(plaintext):
        symbol = plaintext[counter]
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num += key
            if num >= len(LETTERS):
                num -= len(LETTERS)
            ciphertext += LETTERS[num]
        else:
            ciphertext += symbol
        counter += 1
    return ciphertext


def decode(ciphertext, key):
    plaintext = encode(ciphertext, -key)
    return plaintext