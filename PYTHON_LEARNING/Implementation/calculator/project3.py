sum = lambda x,y  :print("sum =",x+y)
sub = lambda x,y  :print("sub =",x-y)
mul = lambda x,y  :print("mul =",x*y)
div = lambda x,y  :print("div =",x/y)
while True:
 print("\noperation you want to perform:\n1\tSum\n2\tSub\n3\tMul\n4\tDiv\n5\tExit")
 op = int(input("operation->\t"))
 x = float(input("Enter a num\t"))
 y = float(input("Enter a num\t"))
 match op:
  case 1:
   print(sum(x,y))
   continue 
  case 2:
   print(sub(x,y))
   continue
  case 3:
   print(mul(x,y))
   continue
  case 4:
   print(div(x,y))
   continue
  case 5:
   break
  case _:
   print("Check input")
  continue