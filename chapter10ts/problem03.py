class demo():
    a = 4
o = demo()
print(o.a) #print class attribute. because instance attribute is not available.
o.a = 0
print(o.a) #print instance attribute because instance attribute is available. 
print(demo.a) #print class attribute.