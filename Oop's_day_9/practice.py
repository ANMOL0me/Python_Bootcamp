'''Create a class Car with a method drive() that prints "Car is moving".
Create an object of Car and call drive().'''

class car:
 def drive(self):
  return "Car is moving"
obj = car()
print(obj.drive())

'''Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
Create an object and print the person’s name and age.'''

class Person:
 def __init__(self,name,age):
  self.age = age
  self.name = name
  print(f"name = {name},\nage = {age}")
obj1 = Person("Anmol",21)

'''Create a base class Animal with a method sound() that prints "Some sound".
Create a derived class Dog that overrides sound() to print "Bark!".
Create an object of Dog and call sound().'''

class Animal:
 def sound():
  return "Some sound"
class Dog(Animal):
 def sound():
  return "BArk!"
obj2 = Dog()
print(obj2.sound()) 