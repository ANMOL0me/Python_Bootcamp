'''3. Static & Class Methods
1. Create a class MathUtils with:

A @staticmethod called add(a, b) that returns a + b.
A @classmethod called description(cls) that prints "This is a utility class for math operations." Call both methods without creating an object.'''

class MathUtils:
 @staticmethod
 def sum(a,b):
  return a+b
 @classmethod
 def description(cls):
  print("This is a utility class for math operations.")

obj = MathUtils()
print(obj.sum(2,5))
obj.description()  
