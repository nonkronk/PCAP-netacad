# Project 3
# Irvan Tristian - 0447356121-105

priority = 1
email = 'irvantristian@gmail.com'

# Encrypt with caesar
def caesar_encript(txt, shift):
    text_list = list(txt)
    for i in range(len(txt)):
        char = text_list[i]
        if char.isalpha() == True:
            asc = ord(char)
            if char.islower() == True:
                text_list[i] = chr((asc - 97 + shift) % 26 + 97)
            else:
                text_list[i] = chr((asc - 65 + shift) % 26 + 65)
    return ''.join(text_list)

# Decrypt with caesar
def caesar_decript(chiper, shift):
    return caesar_encript(chiper, -shift)

# Shuffle order of string
def shuffle_order(txt, order):
    return ''.join([txt[i] for i in order])

# De-shuffle order of string
def deshuffle_order(sftxt, order):
    return ''.join([sftxt[order.index(i)] for i in range(len(order))])

# Encrypt & split encrypted text in to n-char batchs & shuffle chars inside all the batchs
def send_batch(txt, batch_order, shift=3):
    encrypted = caesar_encript(txt, shift)
    n = len(batch_order)
    remainder = len(encrypted) % n
    if remainder != 0:
        for i in range(n - remainder):
            encrypted += "_"
    batchs = [encrypted[i:i + n] for i in range(0, len(encrypted), n)]
    shuffled = [shuffle_order(text, batch_order) for text in batchs]
    return shuffled
    
# De-shuffle encrypted text join all the batchs and decrypt the text 
def receive_batch(batch_cpr, batch_order, shift=3):
    batch_txt = [caesar_decript(deshuffle_order(
        i, batch_order), shift) for i in batch_cpr]
    return ''.join(batch_txt).strip('_')

# Run directly
if __name__ == '__main__':
    
    # Sanity check #1
    msg = 'Haloz DTS mania, MANTAPSZZZ!'
    cpr = caesar_encript(msg, 4)
    txt = caesar_decript(cpr, 4)
    print('plain text:', txt)
    print('chiper text:', cpr)

    # Sanity check #2
    print(shuffle_order('abcd', [2, 1, 3, 0]))
    print(deshuffle_order('cbda', [2, 1, 3, 0]))

    # Sanity check #3
    msg_cpr = send_batch('halo DTS mania, mantaaap!!!', [2, 1, 3, 0], 4)
    msg_txt = receive_batch(msg_cpr, [2, 1, 3, 0], 4)
    print(msg_txt, msg_cpr, sep='\n')
