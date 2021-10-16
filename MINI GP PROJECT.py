print("~"*50)
print("                    HELLO")
print("~"*50)
print("BELOW ARE THE OPERATIONS YOU CAN PERFORM HERE")
print("~"*50)
C="YES"
while C.upper()=="YES":
    print("~"*50)
    print("Enter 1:-TO HAVE WHOLE GP\nEnter 2:-TO HAVE THE SUM OF GP\nEnter 3:-TO HAVE THE NTH TERM FROM GP\nEnter 4:-TO HAVE THE NTH TERM FOR SUM OF GP\nEnter 5:-TO FIND THE FIRST TERM FROM A GP\nEnter 6:-TO FIND FIRST TERM FOR SUM OF GP\nEnter 7:-TO EXIT NOW")
    print("~"*50)
    A=int(input("Enter your choice:-"))
    if A==1:
        a = int(input("ENTER THE 1ST NUMBER:-"))
        b = int(input("ENTER THE COMMON RATIO:-"))
        c = int(input("TILL WHICH TERM YOU WANT THE GP:-"))
        d = 1
        print("~"*50)
        print("THE GP IS BELOW")
        while d <= c:
            e = a * b ** (d - 1)
            print(e, end=" ")
            d += 1
        print()
    elif A==2:
        a = int(input("ENTER THE 1ST NUMBER:-"))
        b = int(input("ENTER THE COMMON RATIO:-"))
        c = int(input("TILL WHICH TERM YOU WANT THE GP:-"))
        d = 1
        S = 0
        while d <= c:
            e = a * b ** (d - 1)
            S += e
            d += 1
        print("SUM OF THE GP IS:-",S)
        print("~" * 50)
    elif A==3:
        a = int(input("ENTER THE 1ST NUMBER:-"))
        b = int(input("ENTER THE COMMON RATIO:-"))
        c = int(input("WHICH TERM YOU WANT:-"))
        g = a * b ** (c - 1)
        print("Nth TERM OF THIS GP IS",g)
        print("~" * 50)
    elif A==4:
        a = int(input("ENTER THE 1ST NUMBER:-"))
        b = int(input("ENTER THE COMMON RATIO:-"))
        c = int(input("ENTER THE SUM OF GP:-"))
        k = (c * (b - 1) + a) // a
        cnt = 0
        while (k // a) != 0:
            cnt += 1
            k = k // a
        print("Nth TERM OF THE SUM OF THIS GP IS:-", cnt)
        print("~" * 50)
    elif A==5:
        a=int(input("ENTER THE COMMON RATIO:-"))
        b=int(input("ENTER THE NUMBER OF TERMS:-"))
        c=int(input("ENTER THE LAST TERM:-"))
        first_term=c//(a**(b-1))
        print("FIRST TERM OF THIS GP IS",first_term)
    elif A==6:
        a=int(input("ENTER THE COMMON RATIO:-"))
        b=int(input("ENTER THE NUMBER TO TERMS:-"))
        c=int(input("ENTER THE SUM OF GP:-"))
        F=(c*(a-1))//(a**b-1)
        print("FIRST TERM OF THIS GP IS",F)
    elif A==7:
        print("~"*50)
        print("                    THANK YOU ")
        break
    else:
        print("INVALID CHOICE!!!!!!")
        print("RE-ENTER YOUR CHOICE:-")
    print("~"*50)
    C=input("Want to do again:-")
    if C.upper()=="NO":
        print("~" * 50)
        print("                    THANK YOU ")
        break