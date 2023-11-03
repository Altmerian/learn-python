def decorator(func):
    def wrapper(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')

    return wrapper


@decorator
def hello(msg):
    print(msg)


hello('Hello')
