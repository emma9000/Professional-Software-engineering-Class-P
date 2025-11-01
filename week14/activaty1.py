"""
This example illustrates the concept of decorators in Python, which are a way to modify or enhance functions or methods. 
In this case, the `log_decorator` adds logging functionality to the `add` function,
printing the function name, its arguments, and the return value each time it is called.
We can just implement a simple decorator method to record logs without changing the original function logic.
And the decorator is run automatically when the decorated function is called.
It will first call the decorator function, then the original function, and finally return the result.
If we don't use the decorator, we need to manually add logging code inside the original function,
which is not fitting for code reusability and separation of concerns.
"""

# Define a decorator that logs function calls
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Apply the decorator to a function
@log_decorator
def add(a, b):
    return a + b


# Call the function
add(3, 5)
