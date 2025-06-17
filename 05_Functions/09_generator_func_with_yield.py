# Question 9 - Grenerator function with yield.
# Statement: Write a generator function that yields even numbers up to a specified limit.


# def even_generator(limit):
#    for i in range(0,limit+1,2): # range(index,end,step)
#       print(i,end=" ")

# even_generator(100)


def even_generator(limit):
   for i in range(0,limit+1,2): 
      # return i # yaha pe return single value return karega esiliye yaha pe yield ka use karte hai 
      yield i

for i in even_generator(100):
   print(i,end=" ")