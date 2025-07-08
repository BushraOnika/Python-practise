import time

def timer(func):

    def wrapper(*args,**kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args,**kwargs)
        end_time = time.perf_counter_ns()
        eclipsed_time = end_time - start_time
        print(result)
        print(f"methord took time: {eclipsed_time:.4f}ns")
        return result

    return wrapper

@timer
def add(a,b):
    return a + b

add(1,2)