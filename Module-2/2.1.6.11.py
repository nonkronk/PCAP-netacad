hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hour = (hour + ((mins + dura) // 60)) % 24
mins = (mins + dura) % 60

print(str(hour) + ":" + str(mins))