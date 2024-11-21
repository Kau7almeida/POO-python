def my_decorator(func):
    def wrapper():
        print('Before the function is called')
        func()
        print('After the function is called')
    return wrapper

@my_decorator
def my_function():
    print('My function was called')

my_function()

class MyDecoratorClass:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:
        print('Before the function is called (class decorator)')
        self.func()
        print('After the function is called (class decorator)')

@MyDecoratorClass
def second_function():
    print('Second function was called')

second_function()