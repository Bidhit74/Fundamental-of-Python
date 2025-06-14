# Question 4: Fruit Ripeness Checker
# Statement: Determine if a fruit is ripe, overipe, or unripe based on its color. (e.g. Banana: Green - Unripe, Yellow - Ripe, Brown - Overipe)

fruit = str(input("Enter the fruits name: "))
fruitColor = str(input("Enter the fruits color name: "))

if(fruit == "Banana"):
    if(fruitColor == "Green"):
        print("Unripe")
    elif(fruitColor == "Yellow"):
        print("Ripe")
    else:
        print("Overipe")