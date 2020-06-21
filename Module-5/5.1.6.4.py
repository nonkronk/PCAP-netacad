def readint(prompt, min, max):
    while True:
        val = input(prompt)
        try:
            val = int(val)
            if val >=  min and val <= max:
                break
            else:
                print(f"Error: the number is not within permitted range ({min}, {max})")        
        except:
            print("Error: wrong input")
    return val

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
