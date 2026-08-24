'''6. map(), filter(), and reduce()
Use map() to convert [1, 2, 3, 4, 5] into their cubes.
Use filter() to get only even numbers from [10, 11, 12, 13, 14].
Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].'''

a = [1,2,3,4,5]
x = list(map(lambda c: c*c*c,a)) 
print(x)
