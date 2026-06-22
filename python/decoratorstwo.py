# Function started
# Hello World
# Function ended
def decorator(func):
    def  wrapper():
        print("function started")
        func()
        print("function ended")
    return wrapper
@decorator
def greet():
    print("hello world")

greet()

# greet=decorator(greet)
# greet()

