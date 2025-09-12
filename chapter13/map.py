from functools import reduce
l = [1,2,3,4,5]
square = lambda n: n*n
sqlist = map(square, l)
print(list(sqlist))

#filter example
def even(n):
    if(n%2 == 0):
        return True 
    return False
onlyEven = filter(even, l)
print(list(onlyEven))

#Reduce example 
def sum(a,b):
    return a + b 

mul = lambda x,y:x*y
print(reduce(mul, l))
