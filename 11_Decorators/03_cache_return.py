# Question 3: Cache Return Values
# Statement: Implement a decorator that caches return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if(args in cache_value):
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        # print(cache_value , args)
        return result
    return wrapper


@cache
def long_runnig_function(a,b):
    time.sleep(2)
    return a * b

print(long_runnig_function(10,5))
print(long_runnig_function(10,5))
print(long_runnig_function(10,10))