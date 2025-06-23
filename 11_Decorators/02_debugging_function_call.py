# Debugging Function Calls
# Statement: Create a decorator to print the function name and the values of its arguments every time the function is called.

# Decorator function create
def debbug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"Key:- {k} and Value:- {v}" for k, v in kwargs.items())
        print(f"Calling function {func.__name__} args_value: {args_value}")
        print(f"Calling function {func.__name__} kwargs_value: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper



@debbug
def hello_fun():
    print("Hello Bidhit")

@debbug
def greet(name,greeting="Hello"):
    print(f"{greeting} {name}")

hello_fun()
greet("Binit","Hi")
greet("Binit",greeting="Hello")