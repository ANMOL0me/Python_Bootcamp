'''x = 10 #Global variable

def my_fun():
 x = 5 # local variable
 print(x)

my_fun()
print(x) '''


def modify_global():
 global x #modifies as global 
 x = 5
 print(x)
modify_global()
print(x)