'''Write a program that takes a list of numbers and removes all duplicates using a set'''
num = [1,2,3,4,2,3,4,3,2,2,3,3,4,]
nums = set(num)
numss = set(num)
print(nums.union(numss))

'''Given a dictionary of products and their prices, find the product with the highest price'''

product = {"apple":33, "mango":44,"banana":55}
ss = list(product.values())
j=0
i=0
while ss[i] >= ss[j]:
 j+=1
 print(ss[i])
 
  
  
   
  
  
