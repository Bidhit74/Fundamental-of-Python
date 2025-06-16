list1 = [1,2,3,4,5]
I = iter(list1) # yaha pe memory ka first reference milta hai
print(I)
print(I.__next__())
print(I) # eska pointer change nahi hota hai yah first ko refer karta hai but value change ho jata hai __next__() use karne se.
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
# print(I.__next__()) # value end hone ka baad agar firse wahi same kaam kiya to 'StopIteration' error dega

print(iter(list1) is list1) # False yah same nahi hai file ki tarah
