alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    global alphabet
    newtext = []
    for i in text:
        if i in alphabet:
            originalindex = int(alphabet.index(i))
            if (originalindex + shift) >= 26:
                originalindex-=26
            elif (originalindex + shift) < 0:
                originalindex+=26
            newtext.append(alphabet[originalindex+shift])
        elif i == ' ':
            newtext.append(i)
        else:
            continue
    encrypted = ''.join(newtext)
    return encrypted

def decrypt(text, shift):
    global alphabet
    newtext = []
    for i in text:
        if i in alphabet:
            originalindex = int(alphabet.index(i))
            if (originalindex - shift) >= 26:
                originalindex -= 26
            elif (originalindex - shift) < 0:
                originalindex += 26
            newtext.append(alphabet[originalindex - shift])
        elif i == ' ':
            newtext.append(i)
        else:
            continue
    decrypted = ''.join(newtext)
    return decrypted

if direction == "encode":
    print(f'The encoded text is {encrypt(text, shift)}')
elif direction == "decode":
    print(f'The decoded text is {decrypt(text, shift)}')
