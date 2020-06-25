def digitof_life(birth):
    sum1 = 0
    for i in birth:
        i = int(i)
        sum1 += i
    sum2 = 0
    for i in str(sum1):
        i = int(i)
        sum2 += i
    return sum2

if __name__ == '__main__':
    birth = input('Birth number: ')
    print(digitof_life(birth))
