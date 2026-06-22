def logger(func):
    def wrapper(name):
        print("function started")
        func(name)
        print("function started")

    return wrapper
@logger
def greet(name):
    print("hello",name)

greet("venkat")