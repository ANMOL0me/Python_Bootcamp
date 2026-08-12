import math
'''1. Defining Functions
>Write a function greet() that prints "Hello, Python Learner!" when called.'''
def greet():
 return "Hello,Python Learner! "
print(greet())

'''Write a function square(num) that returns the square of a given number. Test it with different numbers.'''
def square(num):
 return f"square={num*num}"
print(square(3))


'''2. Function Arguments & Return Values
Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".'''

def full_name(first,last):
 print(f"{first} {last}")
full_name("anmol","soni")
 

'''Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

Both length and width
Only length (use default width)'''
def calculate_area(length,width = 10):
 return length*width
print(calculate_area(2,4))
print(calculate_area(2,))

'''3. Lambda Functions
Write a lambda function that adds two numbers and test it.'''

add = lambda a,b:a+b
print(add(2,4))

'''Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.'''


'''4. Recursion in Python
Write a recursive function factorial(n) that returns the factorial of a number.'''
def factorial(x):
 if(x==1):
  return 1 
 return x*factorial(x-1) 
print(factorial(5))


'''Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number. '''

def sum_of_digit(n):
 if n==0:
  return 0
 return n%10 + sum_of_digit(n//10)
print(sum_of_digit(424))
  
'''5.Import the math module and use it to:

Find the square root of 144
Calculate sin(90°) (hint: use math.radians())
'''

print(math.sqrt(144))
print(math.radians(90))
