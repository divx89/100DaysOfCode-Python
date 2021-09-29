import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        duration = time.time() - start_time
        print(f"Duration is {round(duration, 3)} seconds")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


print("Running Fast Function")
fast_function()

print("Running Slow Function")
slow_function()
