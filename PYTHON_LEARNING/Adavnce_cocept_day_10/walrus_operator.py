#in python 3.5
'''def very_slow():
    print("something..")
    print("something..")
    print("something..")
    print("something..")
    return 20
#a = very_slow()
if( (a:=very_slow()) > 10):
    print(a)
else:
    print("not greater than 10")
    '''

while(data:=input("enter the value")):
    print(data)
    if data=="q":
        break