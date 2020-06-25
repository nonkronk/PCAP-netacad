def encrypt_text(text, shift=1):
    encrypted_text = ''
    for i in range(len(text)):
        char = text[i]
        if not char.isalpha():
            encrypted_text += char
        else:
            if not char.islower():
                asc = ord('A')
            else:
                asc = ord('a')
            enc = asc + ((ord(char) - asc) + shift) % 26
            encrypted_text += chr(enc)
    return encrypted_text


def input_text():
    return input('Text to encrypt: ')

def input_shift():
    while True:
        try:
            shift = int(input('Shift: '))
            if shift >= 1 and shift <= 25:
                break
        except:
            continue
    return shift

if __name__ == '__main__':
    text = input_text()
    shift = input_shift()
    encrypted = encrypt_text(text, shift)
    print(encrypted)
