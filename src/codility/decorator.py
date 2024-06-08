import functools


def decorator_function(decorated):
    @functools.wraps(decorated)  # to disable next 2 lines for decorated function
    def wrapper():
        """wrapper doc"""
        print("I am doing some calcs first!")
        decorated()
        print("I am doing some extra calcs :)")

    return wrapper


@decorator_function
def my_func():
    """my func docs"""
    print('I am going to be decorated *_*')


if __name__ == '__main__':
    print(my_func.__name__)
    print(my_func.__doc__)
    my_func()
