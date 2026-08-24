'''5. Exception Handling and Custom Errors
Write a program that asks the user to enter a number and handles:

ValueError if the input is not a number
ZeroDivisionError if you try to divide by zero'''

try:
    num = int(input("Enter a num:"))
    result = 100 / num

except ValueError:
    print("Error:please enter a valid num.")

except ZeroDivisionError:
    print("cannot divide by zero.")    