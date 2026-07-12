count = 0

while count < 4:
    print(count)
    match count:
        
        case 0:
            for i in range(1, 6):
                print(i)
        case _:
            print("no")
            
    count +=1






