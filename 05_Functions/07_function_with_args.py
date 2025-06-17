# Question 7 - Function with *args
# Statement: Write a function that takes variable number of arguments and return their sum.

# def sum_all(*args):
#    # print(args) # tuple
#    return sum(args)

# or 
def sum_all(*args):
   sum_val = 0
   for i in args:
      sum_val += i
   return sum_val

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8,9))

