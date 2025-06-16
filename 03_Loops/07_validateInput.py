# Question 7 :- Keep asking the user for input until they enter a number between 1 and 10.

while True: # infinite loops ho gaya hai
    num = int(input("Enter the value b/w 1 and 10 : "))
    if 0 < num <= 10: 
        print("Thanks") 
        break
    else: 
        print("Please enter valid input. Try Again !!!")