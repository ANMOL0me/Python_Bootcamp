class parent_class:
 data = "#453"
 def __init__(self):
  print("Want to see data\nY or N\n")
  x = input()
  if(x=='Y' or x=='y'):
   self.show()
  else:
   EXIT 
 def show(self):
  print(f"{self.data}")
class child(parent_class):
 def skip_show(self):
  print(f"{self.data}")
obj = child()
obj.skip_show()
show().parent_class()
    
  
  