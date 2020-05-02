myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

tmpList = []

for i in myList:
    if i not in tmpList:
        tmpList.append(i)

myList = tmpList[:]

print("The list with unique elements only: ")
print(myList)
