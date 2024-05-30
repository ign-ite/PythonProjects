year = int(input("Enter year: "))
leapYear = False
if (year % 4 == 0):
    leapYear = True
    if (year % 100 == 0):
        leapYear = False
    elif (year % 100 == 0) and (year % 400 == 0):
        leapYear = True
if (leapYear == True):
    print("It is a leap year")
else:
    print("It is not a leap year")