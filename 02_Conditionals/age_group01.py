# Question 1. Age Group Categorization
# Statement: Classify a person's age group: Child(< 13), Teanager(13-19), Adult(20-59) and Senior(60+)


age = input("Enter your age: ")
# userAge = age # TypeError: '<' not supported between instances of 'str' and 'int'
userAge = int(age)

if userAge<13:
    print("Child")
elif userAge<20:
    print("Teanager")
elif userAge<60:
    print("Adult")
else:
    print("Senior")