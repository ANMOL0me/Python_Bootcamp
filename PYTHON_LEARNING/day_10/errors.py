while True:
    try:
        a = int(input("Enter a num 1"))
        b = int(input("Enter a num 2"))
        print(f"The sum is {a + b}")
    except Exception as e:
        print(e) 
    if b == 0:
        raise ValueError("dont do this")    