'''def decorator(func):
 def wrapper():
  print("I am about to print hello...")
  func()
  print("I have executed")
 return wrapper

def say_hello():
 print("Hello")
f = decorator(say_hello)
f() 
def fun1(fun2):  #1 argument passes
 def funo(): #  3 function calls
  print("1") # 4 this prints
  fun2()     # 5 function calls fun2 = day_hello
  print("3") # 6 this prints
 return funo  # 2 returns funo
def day_hello():
 print("hello")
f = fun1(day_hello) # f is fun1 function with argument day_hello fun
f() #it calls f  '''

def repeat(n):
 def decorator(func):
  def wrapper(a):
   for i in range(n):
    func(a)
  return wrapper 
 return decorator

@repeat(2)
def hel(a):
 print(f"hello! {a}")
hel("mmm")

