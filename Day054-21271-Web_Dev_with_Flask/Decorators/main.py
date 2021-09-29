import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # [1] Do something before calling the function
        function()
        # [2] Call the function multiple times
        # [3] Do something after calling the function

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


# Calling say_hello, we see that it gets a 2 second delay
say_hello()

# Calling say_greeting, there is no delay
say_greeting()
