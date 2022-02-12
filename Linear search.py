a=list(eval(input("Enter the list:-")))
    s=int(input("Enter the value to be searched:-"))
    for i in range(len(a)):
        if a[i]==s:
            break
    print(s,"found at position:-",i+1)