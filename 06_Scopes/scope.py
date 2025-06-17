# Scope or Namespace in python

username = "Bidhit" # Globle Scope or Variable

def func():
   print(username)
   username = "Binit" # Local Scope or Variable
   print(username)

print(username)

x = 98

def func2():
   x = 60 # local variable

func2()
print(x)

def func3():
   global x # es se hum globle variable ko change kar sakte hain but esa nahi karna
   x = 60 # local variable

func3()
print(x) # now change globle value 


y = 98

def f1():
   y = 88
   def f2():
      print(y)
   return f2 # reference ko return kar dega

print(f1()) # f2 reference mila hai
myResult = f1()
myResult() # now print 88


# Closer Property
def outer(num):
   def inner(x):
      return x ** num
   return inner

print(outer(5))
result = outer(7)
print(result(2))  # prints 128, which is 3^7

F = outer(3)
g = outer(4)

print(F(2))  # prints 8, which is 2^3
print(g(2))  # prints 16, which is 2^4

