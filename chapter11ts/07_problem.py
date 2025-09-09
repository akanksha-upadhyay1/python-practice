class Vector:
    
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
    def __str__(self):
        return f"Vector: {self.l}"
    
#test the implementation
v1 = Vector([1,2,3])
print(len(v1))