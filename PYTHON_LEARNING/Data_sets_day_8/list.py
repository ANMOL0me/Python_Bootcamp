'''# list
my_list = [1,2,3,4]
mixed = [10,"hello",3.14]
# list method
my_list.append(4)
print(my_list)
my_list.insert(4,44) #duplicate files dont show
my_list.remove(3) 
my_list.pop() #remove last element
my_list.reverse()
my_list.sort()


my_list = [1,2,4,6]
my_list.append(8) 
print(my_list)
my_list.insert(8,9)
print(my_list)
'''
'''
#table of 2
table = []
for i in range(0,11):
 table.append(2*i)
print(table)
'''
# list comprehension

table = [2*i for i in range(0,11)]
print(table)
