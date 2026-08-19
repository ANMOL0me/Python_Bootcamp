while True:
    try:
        a = int(input("ENter a num 1"))
        b = int(input("ENter a num 2"))
        print(f"The sum is {a + b}")
    except Exception as e:
        print(e)