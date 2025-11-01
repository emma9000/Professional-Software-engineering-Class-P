'''
1. Create a decorator that measures the execution time of a function.
2. The process after processing the program:
    - When the decorated function is called, the decorator should print a message indicating the start of execution.
    - It should then record the start time, call the original function, and record the end time after the function completes.
    - Finally, it should calculate and print the total execution time before returning the result of the original function.
'''

import time
# Define a decorator that measures execution time
def time_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"decorator: Starting execution of {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"decorator: {func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

# Apply the decorator to a function
@time_decorator
def simulate_task(a,b):
    print("simulate_task: Simulating a time-consuming task...")
    sum=a+b
    time.sleep(2)  # Simulate a time-consuming task
    print("simulate_task: Task completed.")
    return sum

# Call the function
simulate_task(10,20)