def is_anagram(text1, text2):
    if len(text1) != len(text2):
        return False
    else:
        text1 = text1.lower()
        text2 = text2.lower()
        list1 = []
        list2 = []
        for i in range(len(text1)):
            list1.append(ord(text1[i]))
            list2.append(ord(text2[i]))
        list1.sort()
        list2.sort()
        return list1 == list2


if __name__ == '__main__':
    text1 = input('Text 1: ')
    text2 = input('Text 2: ')
    if not is_anagram(text1, text2):
        print('Not anagrams')
    else:
        print('Anagrams')
