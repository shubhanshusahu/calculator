while True:
    a=float(input("Enter a number"))
    b=float(input("Enter a number"))
    if a==0 or b==0:
        print("invalid input")
        break
    else:  
        print(" for addition enter 1:")
        print(" for substact enter 2:")
        print(" for multiply enter 3:")
        print(" for division enter 4:")
        cout=int(input("enter your choice"))
        if cout==1:
            print("addition result= ",a+b)
        elif cout==2:
            print("substraction result= ",a-b)
        elif cout==3:
            print("multiplication result= ",a*b)
        elif cout==4:
            print("division result= ",a/b)
        else:
            print("wrong choice try again")#added comment to check pull command
