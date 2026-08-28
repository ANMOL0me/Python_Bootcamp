'''2. Read, Write, and Append Files
Write a program that writes three lines of text to a file tasks.txt.
Open tasks.txt in append mode and add a new line "Task Completed!".
Read the file and print all lines as a list using readlines().'''



file = open("tasks.txt","a")
file.write("Task Completed!")
file.close()
file = open("tasks.txt","r")
for line in file:
 print(line)
 

