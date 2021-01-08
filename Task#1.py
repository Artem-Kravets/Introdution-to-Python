def count_function_calls_decorator(func):
    def wrapper(*args):
        wrapper.calls += 1
        return func(*args)

    wrapper.calls = 0
    return wrapper


@count_function_calls_decorator
def nameless_function(x):
    return x


nameless_function(0)
nameless_function(1)
nameless_function(2)
nameless_function(3)
nameless_function(4)
nameless_function(5)

print(nameless_function.calls)

