class animals:
    pass

class pets(animals):
    pass 

class Dog(pets):
    @staticmethod
    def bark():
        print("bow bow")

d = Dog
d.bark()