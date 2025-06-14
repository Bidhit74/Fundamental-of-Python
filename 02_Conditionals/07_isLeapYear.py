# Question 7: Leap year checker
# Statement: Determine if a year is a leap year :(leap year are divisible by 4, but not by 100 unless also divisible by 400)

year = int(input("Enter the year : "))
# isLeapYear = False

# if year % 400 == 0:
#     isLeapYear = True
# elif year % 4 == 0:
#     if year % 100 != 0:
#         isLeapYear = True


# if isLeapYear == True:
#     print("leap Year")
# else:
#     print("Not leap year")

# or

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, ": Leap year!!!")
else:
    print(year,": NOT Leap year!!!")