fn = input('Enter filename: ')

try:
    f = open(fn, 'rt', errors='ignore')
    letter = {}
    for i in range(ord('a'), ord('a') + 26):
        letter[chr(i)] = 0
    for line in f:
        for ch in line.lower():
            if ch in letter.keys():
                letter[ch] += 1
    for k, v in letter.items():
        if v != 0:
            print(k, '->', v)

except Exception as e:
    print(e)
