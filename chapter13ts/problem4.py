def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [ 1, 2, 45, 645, 650, 45360]

f = list(filter(divisible5, a))
print(f)