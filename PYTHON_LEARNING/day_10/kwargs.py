# kwarg is a dictionary

def marks(**kwargs):
    for item in kwargs.keys():
        print(f"item = {item} is {kwargs[item]}")

marks(ahubham = 55,vkd= 3)
def fun(*args,**kwargs):
    print(args)
    print(kwargs)

fun(1,2,3,4,jack=34,kk=55)