#programe to check a number is the factor of another number or not
num=int(input("Enter the main number:-"))
factor=int(input("Enter the divisior:-"))
if factor>num:
    print("Your main number shoud be greater!!!!")
elif factor==0:
    print("Division by zero is not allowed !!!!")
else:
    if num%factor==0:
        print(factor,"is the factor of",num)
    else:
        print(factor,"is not the factor of",num)