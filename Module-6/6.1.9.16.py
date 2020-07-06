fn = input('Enter filename: ')

try:
    fo = open(fn, 'rt', errors='ignore')
    letter = {}
    for i in range(ord('a'), ord('a') + 26):
        letter[chr(i)] = 0
    for line in fo:
        for ch in line.lower():
            if ch in letter.keys():
                letter[ch] += 1
    fo.close()
    sorted_letter = sorted(letter.items(), key=lambda x: x[1], reverse=True)
    fw = open(fn + '.hist', 'wt')
    for i in sorted_letter:
        if i[1] != 0:
            line = str(i[0]) + ' -> ' + str(i[1])
            print(line)
            fw.write(line + '\n')
    fw.close()

except Exception as e:
    print(e)
