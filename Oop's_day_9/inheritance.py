class parent_class:
def show(self): #overdiding
  
  print(f"{self.data}")
 


class child(parent_class):  #inheritance
data = "#453"
 def __init__(self):
  print("Want to see data\nY or N\n")
  x = input()
  if(x=='Y' or x=='y'):
   self.show()
  else:
   pass 
 def show(self):
  super().show()
  print("vip method") 
obj = child()
obj.show()

    
  
  