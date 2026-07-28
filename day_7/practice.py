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
 

'''
Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

Both length and width
Only length (use default width)'''
