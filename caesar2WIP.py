from typing import List, Any
#This will only do encryption and not decryption
#not sure what is happening with that
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = 'decode' # input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = 'beans' # input("Type your message:\n").lower()
shift = 5 # int(input("Type the shift number:\n"))

def indexbounds(originalindex, shift):
    if (originalindex + shift) >= 26:
        originalindex -= 26
    if (originalindex - shift) < 0:
        originalindex += 26

def caesar(direction, text, shift):
    global alphabet
    newtext = []
    if direction == "encode" or "encrypt":
        encrypted = False
    elif direction == "decode" or "decrypt":
        encrypted = True
    for i in text:
        if i in alphabet:
            originalindex = int(alphabet.index(i))
            if encrypted == False:
                indexbounds(originalindex, shift)
                newtext.append(alphabet[originalindex+shift])
            else:
                indexbounds(originalindex, shift)
                newtext.append(alphabet[originalindex-shift])
        elif i == ' ':
            newtext.append(i)
        else:
            continue
    answer = ''.join(newtext)
    return answer

caesar(direction, text, shift)
print(f'The {direction}d text is {caesar(direction, text, shift)}')
