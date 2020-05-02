c0 = int(input("Enter a number: "))

counter = 0
while True:
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
        counter += 1
    else:
        c0 = 3 * c0 + 1
        print(c0)
        counter += 1
    if c0 != 1:
        continue
    else:
        break

print("steps =", counter)
