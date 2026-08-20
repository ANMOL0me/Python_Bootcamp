#variable arguments
#args collects all values and make it into tuple
def sum(*args):
    total = 0
    for item in args:
        total += item
    return total    

#print(sum(342,2))
print(sum(342,2,4,5))