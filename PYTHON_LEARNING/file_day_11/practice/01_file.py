'''1. File I/O Basics
Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
Open notes.txt, read its content, and print it to the console.'''
f = open("notes.txt","r")

c = f.read()
print(c)
f.close()

