
print("Enter plain text:")
plainText = input().upper()

print("Enter encryption key: ")
key = int(input())

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encrypted = ""

counter = 0
while counter < len(plainText):
    symbol = plainText[counter]
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = num + key
        if num >= len(LETTERS):
            num = num - len(LETTERS)

        encrypted = encrypted + LETTERS[num]

    else:
        encrypted = encrypted + symbol

    counter+= 1

print(encrypted)