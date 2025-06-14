# Question 6: Coffee Customization
# Statement: Customize a coffee order: "small", "medium" or "large" with an option for "Extra shot" of espresso

order_size = str(input("Enter the coffee size: ")).lower() 
isShot = str(input("You need extra shot: ")).lower() 

if(isShot=='yes'):
    coffee = "Your Coffee size: " + order_size + " with extra shot."
else:
    coffee = "Your Coffee size: " + order_size

print(coffee)