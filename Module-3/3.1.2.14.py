blocks = int(input("Enter the number of blocks: "))

height = 0
while True:
    height += 1
    blocks -= height
    if blocks == 0:
        break
    if blocks < 0:
        height -= 1
        break

print("The height of the pyramid:", height)
