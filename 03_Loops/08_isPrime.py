# Check Prime or Not

num = int(input("Check prime, Enter the number: "))
x = int(num/2)
isPrime = True
while x>1:
    if num % x == 0:
        isPrime = False
        break
    x -= 1

if(isPrime == True):
    print(num, "is Prime")
else:
    print(num, "is NOT Prime")

