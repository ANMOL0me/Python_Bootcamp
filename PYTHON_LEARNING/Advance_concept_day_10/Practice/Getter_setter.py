'''2. Getters and Setters
Create a class Employee with a private attribute _salary.

Use @property to define a getter for salary.
Use @salary.setter to prevent setting negative values (print a warning instead).
Create an object and test by setting positive and negative salaries.'''



class Employee:
 def __init__(self,salary):
  self._salary = salary
@property
def salary(self):
 return self._salary

e = Employee(-10000) 
print(e)


