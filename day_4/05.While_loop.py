count = 0

while count < 4:
    print(count)
    count +=1
count = 0
for i in range(1, 6):
    print(i)

match count:
    case 0:
        print(count)
    case _:
        print("no")


