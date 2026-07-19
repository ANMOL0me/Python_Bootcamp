'''
Create a string variable name with your full name. Print:

The first character
The last character
The length of the string
'''
var = "print"
print(var[0])
print(var[-1])
print(len(var))

'''
Concatenate two strings: "Hello" and "World" with a space in between.
'''

str1 = "hello"
str2 = "world"

print(str1,str2)
'''
Given text = "Python Programming", do the following:

Print the first 6 characters
Print the last 6 characters
Print every second character from the string
'''
text = "Python Programming"
print(text[0:6])
print(text[-6:]) #if we leave mwans length
print(text[::2])

'''
Reverse the string text using slicing.
'''
print(text[::-1])