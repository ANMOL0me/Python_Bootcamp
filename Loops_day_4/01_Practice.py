#Program that print 
'''
#Q1: Your First Program
Write a program that prints:
Hello, World! Welcome to Python.
'''
print("Hello, World! Welcome to Python\n")

'''
Q2: Print a Poem
Write a program that prints the following poem using a single print() statement:
(Hint: Use \n for a new line.)
Twinkle, twinkle, little star,
How I wonder what you are!
'''
print("Twinkle, twinkle, little star\nHow I wonder what you are!")


'''
Q3: Variables & Data Types
Create variables to store:

Your name (string)
Your age (integer)
Your height in meters (float)
A boolean value representing whether you are a student
Print all of them in one line.
'''
name = str(input("your_name\t"))
age = int(input("your_age\t"))
height = float(input("your_height\t"))

is_student = True
print("Name is \t"+name+"\nAge is\t\t",age,"\nHeight is\t",height)


'''
Q4: Typecasting Practice
You are given a string:
num = "45"
Convert it into an integer
Add 10 to it
Print the result
'''
num = "45"
num = int(num)
print(num+10)
'''
Q5: Taking User Input
Write a program that:
Asks the user for their favorite food.
Prints:
Wow! I also like <food>.
'''
food = input("Favourite_Food\t")
print("Favourite food = ",food)

'''
Q6: Simple Calculator
Write a program that:
Takes two numbers as input from the user.
Prints their:

Sum
Difference
Product
Quotient

'''
num1 = float(input("Enter no. 1\t"))
num2 = float(input("Enter no. 2\t"))
print("SUM = ",num1 + num2)
print("DIFF = ",num1 - num2)
print("PROD = ",num1 * num2)
print("QUOT = ",num1 / num2)
'''
Q7: Escape Sequences
Print the following output using escape sequences:
Hello "Python" World!
This is on a new line.
This is a tab →	    after tab.
'''
print("Hello \"Python\" World!\nThis is on a new line.This is a tab →\t after tab.")

'''
Q8: Operator Challenge
Write a program that:
Takes an integer as input from the user.
Prints the square and cube of that number.
'''
num = int(input("enter a num\t"))
print("Square of num =",num**2,"\nCube of num =",num**3)

