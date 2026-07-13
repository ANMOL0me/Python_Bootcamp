
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

'''
2. Match Case Statements
Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
'''
day = int(input("Enter a day"))
if (day>=1):
    match day:
        case 1:
            print("MONDAY")
        case 2:
            print("TUESDAY")
        case 3:
            print("WEDNESDAY")
        case 4:
            print("THRUSDAY")    
        case 5:
            print("FRIDAY")
        case 6:
            print("SATURDAY")
        case 7:
            print("SUNDAY")                        

'''
Write a program using match case that simulates a simple calculator.
Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case.
'''
num1 = float(input("Enter a num\t"))
op = str(input("Enter a operation"))
num2 = float(input("Enter a num"))
match op:
    case "+":
        print("sum =/t",num1+num2)
    case "-":
        print("sum =/t",num1-num2)
    case "*":
        print("sum =/t",num1*num2)        
    case "/":
        print("sum =/t",num1/num2)

'''
3. For Loops
Print numbers from 1 to 10 using a for loop.
'''
for i in range(1,11):
    print(i)

'''
Print the multiplication table of a number (entered by user).
'''
num1 = int(input("Enter a num for table"))
for i in range(1,11):
    print(i*num1)

'''
Calculate the sum of all numbers from 1 to 100 using a for loop.
'''
x=0
for i in range(101):
    print("x =",x,"\ti=",i,"\t=",x+i)
    x = x+i
    
'''
Print the following pattern using a for loop:
*
**
***
****        
'''

for i in range(1,5):
    print("*"*i)
    

'''
4. While Loops
Print numbers from 1 to 10 using a while loop.
'''
x=1
while x<=10:
    print(x)

'''
Write a program that keeps asking the user to enter a password until they enter the correct one.
'''
print("pass is between 1 to 10")
while True:
    pasw=int(input("Enter pass\t"))
    if pasw==5:
        print("pass correct")
        break
    elif pasw!=5:
        print("pass incorrect")
        continue
    

'''
Use a while loop to reverse a given number (e.g., 123 → 321).

'''
num=123
print(int(str(num)[::-1]))