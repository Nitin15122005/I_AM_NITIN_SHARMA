print("~"*50)
print("Solve differentiation and Integration easily here !!!!")
print("~"*50)
print("For eg.:- 4x^2       \n1.HERE 4 IS CONSTANT \n2.X IS THE VARIABLE\n3.2 IS THE POWER OF VARIABLE")
print("~"*50)
what=input("What you want to do (differentiation/integration):- ")
if what.upper()=="DIFFERENTIATION":
    constant=input("Enter the value of constant(IF ANY):- ")
    if int(constant)==0:
        print("The differentiation will be 0")
    else:
        power=input("Enter the value of power:- ")
        con=eval(constant)*eval(power)
        pow=eval(power)-1
        print("DIFFERENTIATION IS",str(con)+"x^"+str(pow))
        print("~"*50)
        want=input("WANT TO PUT VALUE OF X :- ")
        if want.upper()=='YES':
            X=input("ENTER THE VALUE OF X:- ")
            NOW=con*(eval(X)**pow)
            print("~"*50)
            print("FINAL RESULT:-",NOW)
if what.upper()=="INTEGRATION":
    cons=input("ENTER THE VALUE OF CONSTANT(IF ANY):- ")
    if int(cons)==0:
        print("THE INTEGRATION IS 0")
    else:
        powe=input("ENTER THE VALUE OF POWER:- ")
        n=eval(powe)+1
        text=cons+"x^"+str(n)+"+C"
        te=str(text)
        print("INTEGRATION IS:- ","\u0332".join(te),"\n                    ",n)
        want=input("WANT TO PUT UPPER AND LOWER LIMIT:- ")
        if want.upper()=="YES":
            U=int(input("ENTER THE UPPER LIMIT:- "))
            L=int(input("ENTER THE LOWER LIMIT:- "))
            T=U-L
            s=eval(cons)
            p=s+T**n
            upper=str(p)+"+C"
            t=str(upper)
            print("INTEGRATION IS:- ","\u0332".join(t),"\n                   ",n)