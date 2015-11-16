__author__ = 'Code Hobbits'

import iCaesar


print("Enter plain text:")
pt = input().upper()

print("Enter encryption key: ")
cipherKey = int(input())

ct = iCaesar.encode(pt, cipherKey)

print(ct)



