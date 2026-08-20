from functools import reduce
def sum(a,b):
    return a+b
a = [1,2,3,23,4,21,3,42,42]
#3,3,23,4,21,3,42,42
#6,23,4,21,3,42,42
#29,4,21,3,42,42
c = reduce(sum,a)
print(c)