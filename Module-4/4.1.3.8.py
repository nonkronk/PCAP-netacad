def isYearLeap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def daysInMonth(year, month):
    leapMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) == True and month == 2:
        return 29
    return leapMonth[month - 1]


def dayOfYear(year, month, day):
    totalDays = 0
    for i in range(month - 1):
        totalDays += daysInMonth(year, i + 1)
    if day > daysInMonth(year, month):
        return None
    return totalDays + day

print(dayOfYear(2000, 12, 31), end="\n\n")

testYears = [2000, 2000, 2001, 2001]
testMonths = [12, 2, 2, 11]
testDays = [31, 29, 29, 30]
testResults = [366, 60, None, 334]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    dy = testDays[i]
    print(dy, mo, yr, "= ", end="")
    result = dayOfYear(yr, mo, dy)
    if result == testResults[i]:
        print(str(result), "-> OK")
    else:
        print(str(result), "-> Failed")
    
