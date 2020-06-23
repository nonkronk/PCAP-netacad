def mysplit(strng):
    result = []
    text = ''
    for i in range(len(strng)):
        if strng[i] != ' ':
            text += strng[i]
        else:
            if text == '':
                continue
            result.append(text)
            text = ''
        if i == len(strng) - 1 and text != '':
            result.append(text)
    return result

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
