# Decorator - Decorators ek toll ki tarah hota jaise har gari toll se pass hota hai waise hi jab decorator use karte hai tab jis function pe decorator use karte wah function decorator ke andar pass ho ke jaata hai

# Question 1: Timing Function Exexution
# Statement: Write a decorator that measures the time a function takes to execute.

import time

def my_timer(func):
    def wrapper(*args, **kwargs):
        strat_time = time.time()
        result = func(*args,**kwargs) # function execute
        end_time = time.time()
        print(f"{func.__name__} run time is {end_time-strat_time} second.")
        return result
    return wrapper


@my_timer # this my decorators - now example_function pass my_timer function
def example_function(n):
    time.sleep(n)

example_function(5)



