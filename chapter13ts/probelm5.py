from functools import reduce
a = [ 1, 2, 45, 645, 650, 45360]
def greater(a,b):
    if (a>b):
        return a
    return b 

print(reduce(greater,a))