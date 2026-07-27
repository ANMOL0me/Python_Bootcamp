#POSITIONAL ARGUMENTS
def add(a,b):
 return a+b
print(add(3,4))

#DEFAULT ARGUMENTS
'''print("code = \ndef add(a = 2 , b = 3):\nreturn f'sum={a+b}'\nprint(add())")'''

def add(a = 2 , b = 3):
 return f"sum ={a+b}"
print(add())

#KEYWORD ARGUMENT
def Student(name,age):
 print(f"Name:{name} , Age:{age}")
Student(age= 29, name="bb")