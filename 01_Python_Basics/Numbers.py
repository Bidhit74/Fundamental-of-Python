import math
x = 2
y = 3
z = 4

print(z-x)
print(z**y) # z power y
print(x + y * z) 
print(float(40) + 2.34) # python mismatch data type handle kar leta hai lekin explicit data use kare same data type bana ke liye jo ek achha practice hai
print('Bidhit' + ' Kumar') # operator overloading
print(x,y,z)
print(math.floor(3.5)) # 3
print(math.floor(-3.5)) # -4
print(math.floor(3.9)) # 3
print(math.floor(-3.9)) # -4
print(math.floor(-3.1)) # -4
print(math.trunc(2.8) )# 2
print(math.trunc(-2.8)) # -2

print(0.1 + 0.1 + 0.1 - 0.3)
#5.551115123125783e-17
print((0.1 + 0.1 + 0.1) - 0.3)
#5.551115123125783e-17
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))