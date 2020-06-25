def is_palindrome(text):
    rvrsd_text = text[::-1].replace(' ','').lower()
    print(rvrsd_text)
    print(text.replace(' ','').lower())
    return rvrsd_text == text.replace(' ','').lower()

def input_text():
    while True:
        text = input('Text: ')
        if not text.replace(' ','').isalpha():
            continue
        else:
            break
    return text

if __name__ == '__main__':
    text = input_text()
    if not is_palindrome(text):
        print(text, 'is not a palindrome')
    else:
        print(text, 'is a palindrome')
