mydict = {'a':1, 'b':2, 'c':3}

# for key in mydict.keys():
#     print(key)

I = iter(mydict)
print(I.__next__())
# or
print(next(I))
print(next(I))
