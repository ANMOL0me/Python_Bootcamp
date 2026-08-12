def decorator(func):
 def wrapper():
  print("I am about to print hello...")
  func()
  print("I have executed")
 return wrapper

def say_hello():
 print("Hello")
f = decorator(say_hello)
f()

