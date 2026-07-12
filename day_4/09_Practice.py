''' 
If-Else Conditional Statements
Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
'''
num = float(input("Enter a number\n"))
if (num>=0):
    print("num is positive")
elif (num<0):
    print("num is negative")
else:
    print("incorrect input")        

'''
Create a program that checks if a person is eligible to vote (age >= 18).
'''
age = int(input("Enter your age"))
if age>=18:
    print("you are eligible")
else:
    print("not eligible")
        
'''
Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
'''
while True:
    num = float(input("enter a num"))
    if ((num//2) == 0):
        print("num is even")
        continue
    else:
        print("num is odd")
        continue    