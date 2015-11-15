__author__ = 'Code Hobbits'

# Write a program to encrypt a message to morse code and decrypt it back to alphanumeric
# The length of a dot is one unit
# A dash is three units
#  the space between parts of the same letter is one unit
#  the space between letters is three units
#  the space between words is seven units

import sys
import re

morseCode = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '       '
}


def encode(m):
    charpos = 0
    s = ""
    while charpos < len(m):
        letter = m[charpos]
        # if the letter is not found in morseCode dictionary, exit python
        if letter not in morseCode:
            sys.exit("Character cannot be translated to Morse Code")
        s = s + morseCode[letter] + "   "
        charpos += 1
    return s


print("Enter the message you want to encode: ")
message = input().upper()
secretMessage = encode(message)
print(secretMessage)
