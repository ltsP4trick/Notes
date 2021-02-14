def decorator(func):
    def wrapper():
        print("--------")
        func()
        print("--------")
    return wrapper

#option 1
def hello():
    print("hello world")
hello = decorator(hello)
hello()

print("\n\n\n")

#option 2
@decorator
def hello2():
    print("hello world")
hello2()