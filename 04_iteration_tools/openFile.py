# File automatic iter() object esiliye iter keyword nahi use karte hai

# f = open('myFile.py')
# print(iter(f) is f) # ask dono same // file by default iter() ka use karta hai
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline()) # esko end ka pata hota hai NO Error

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__()) # esko end ka nahi pata hota: error - StopIteration

# for loops in file
# for line in open("myFile.py"):
#     print(line)

# while loops
# f = open('myFile.py')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line,end='')

# not key word uses
# test = "Bidhit"
# test = ""
# if not test:
#     print("Hello Bidhit")