class calculator:

    def __init__(self, n):
        self.n = n
    
    def square(self):
       print(f"the square is {self.n*self.n}")
    
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"the sqaureroot is {self.n**1/2}")


a = calculator(3)
a.square()
a.cube()
a.squareroot()