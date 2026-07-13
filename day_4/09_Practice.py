
for i in range(1,10):
    print(i)
    if i==7:
        break
    else:
        continue


'''
Print numbers from 1 to 10, skipping the number 5 (use continue).
'''
for i in range(1,11):
    if i!=5:
        print(i)
    else:
        continue    

'''
Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
'''

for i in range(1,6):
    if i==3:
        pass
    print(i)