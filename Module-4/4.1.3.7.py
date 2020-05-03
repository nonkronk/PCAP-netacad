def isYearLeap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def daysInMonth(year, month):
    leapMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) == True and month == 2:
        return 29
    return leapMonth[month - 1]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
