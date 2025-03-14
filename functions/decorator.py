def decorator(func):
    def wrapper(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')

    return wrapper

def f(msg):  
    print(msg)

w = decorator(f)
w("Hello")


@decorator
def hello(msg):
    print(msg)

hello('Hello')
