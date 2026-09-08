import operation
try:
 while(1): 
   n1 = input("Enter a num = ")
   while(n1=="exit"):
    exit() 
   op = input("operation  = ")
   while(op=="exit"):
    exit()
   n2 = input("Enter a num = ")
   while(n2 =="exit"):
    exit()
   try:
    n1 = int(n1)
    n2 = int(n2)
   except ValueError:
    raise ValueError("Check number")
   match op:
    case "+":
     print(operation.Add(n1,n2))
    case "-":
     print(operation.Sub(n1,n2))
    case "*":
     print(operation.Mul(n1,n2))
    case "/":
     print(operation.Div(n1,n2))
    case _:
     print("Invalid operation")
except Exception as e:
 print(e)