class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


# We're using variable arguments here,
# and calling index 0 to get the User object passed
# We have to ensure that the 1st argument passed by the decorator
# is always a User object
def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])  # The 1st argument to function() has to be User object

    return wrapper


@is_authenticated
def create_blog_post(user: User):
    print(f"This is {user.name}'s new blog post")


def logging_decorator(function):
    def wrapper(*args):
        print(f"Function name is {function.__name__}")
        print(f"Function arguments are {args}")
        result = function(args[0], args[1])
        print(result)

    return wrapper


new_user = User("DivX")
new_user.is_logged_in = True
create_blog_post(new_user)


@logging_decorator
def get_sum(num1, num2):
    return num1 + num2


get_sum(3, 2)
