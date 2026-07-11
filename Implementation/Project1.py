print("----------------CALCULATOR----------------")
print("Addition = '+'\nSubtraction = '-'\nDivision = '/'\nMultiplication = '*'\nExponential = '**' ")
but = str(input("To proceed press p"))
if(but == "p"):
    num1 = float(input("Enter num1=\t"))
    op = str(input("operation to be performed=\t"))
    num2 = float(input("Enter num2=\t"))
    if (op=="+"):
        print("Sum =\t",num1+num2)
    elif (op=="-"):
        print("Diff =\t",num1-num2)
    elif (op=="*"):
        print("Mul =\t",num1*num2)
    elif (op=="/"):
        print("Div =\t",num1/num2)
    elif (op=="**"):
        print("Expon =\t",num1**num2)
    else:
        print("check the input") 