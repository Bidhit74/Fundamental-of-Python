# Question:03 :: Grade Calculator
# Statement: Assign a letter grade based on a student's score: O(90-100),        A(80-89), B(70-79), C(60,69), D(50,59) and F(Below 50)

score = int(input("Enter you score: "))

if(score>100):
    print("Please check you score again!!!")
    exit()

if(score >= 90):
    print("Your grade is: O")
elif(score >= 80):
    print("Your grade is: A")
elif(score >= 70):
    print("Your grade is: B")
elif(score >= 60):
    print("Your grade is: C")
elif(score >= 50):
    print("Your grade is: D")
else:
    print("Your grade is: F")