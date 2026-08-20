#dunder = double underscore
class Employee:
 def __init__(self,name,salary):#magic method
  self.name = name
  self.salary = salary
 
 def __str__(self): #dunder
  return f"name is {self.name}"
  
 def __repr__(self):
  return f"{self.name}" 

e = Employee("ssss",43222)
print(len(e.name))
print(e.name , e.salary)
print(str(e))
print(repr(e))