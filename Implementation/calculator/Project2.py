def sum(a,b):
 return f"sum = {a+b}"
def sub(a,b):
 return f"sub = {a-b}"
def mul(a,b):
 return f"Mul = {a*b}"
def div(a,b):
 return f"Div = {a/b}"
a = float(input("Enter a num:\t"))
b = float(input("Enter a num:\t"))
print("\nWhat operation you want to perform:\n1\tSum\n2\tSub\n3\tMul\n4\tDiv")
op = int(input("->\t"))
match op:
 case 1:
  print(sum(a,b)) 
 case 2:
  print(sub(a,b))
 case 3:
  print(mul(a,b))
 case 4:
  print(div(a,b))
 case _:
  print("Check input")