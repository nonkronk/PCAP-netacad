def isPrime(num):
    counter = 0
    for i in range(num):
        if num % (i + 1) == 0:
            counter += 1
    if counter == 2:
        return True
    return False

for i in range(1, 20):
	if isPrime(i + 1):
	    print(i + 1, end=" ")
print()
