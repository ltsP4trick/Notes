class Dog:
    def __init__(self, name):
        self.dogname = name
        print(name)

    def behavior(self):
        print("woof")
        print("my name is {}".format(self.dogname))


pel = Dog("Ares")
print(pel.behavior())