#higher order functions.
num = [1,2,3,4,54]
#def square(x):
 #   return x*x

#new = list(map(square,num))
new = list(map(lambda x: x*x,num))
print(new)
