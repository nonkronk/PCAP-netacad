def pos(text1, text2):
    matched = 0
    for t1 in text1:
        if text2.find(t1) == -1:
            continue
        else:
            matched += 1
    return matched == len(text1)


if __name__ == '__main__':
    text1 = input('Text1: ')
    text2 = input('Text2: ')
    check = pos(text1, text2)
    if not check:
        print('No')
    else:
        print('Yes')
