class Employee:
 company = "HP"
 def __init__(self,name,salary):
  self.name = name
  self.salary = salary
 def print_info(self):
  print(f"the name is {self.name} and salary is {self.salary}")
 @staticmethod 
 def sum(a,b):
  return a + b
 @classmethod
 def print_company(cls):
  print(cls.company)
 
e1 = Employee("jack",5422)
e2 = Employee("jill",4444) #instance method
#print(Employee.company)
e1.print_info()
e2.print_info()
print(e2.sum(2,3))
print(Employee.sum(2,3))
e1.print_company()