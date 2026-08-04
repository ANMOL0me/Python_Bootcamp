'''
Create a list fruits = ["apple", "banana", "cherry"].

Print the first fruit.
Replace "banana" with "orange".
Print the length of the list.

'''
#list
fruits =["apple","banana","cherry"]
print("\n",fruits)
print(fruits[0])
print(len(fruits)) 
fruits[1] = "orange"
print(fruits,"\n")
'''Create a list of numbers from 1 to 10.

Print the first three numbers using slicing.
Print the last three numbers using slicing.'''

list1 = [i for i in range(1,11)]
print(list1)
print(list1[0:3])
list1.reverse()
print(list1[0:3])
