print("~"*70)
print("HERE YOU CAN CONVERT THE VALUES OF BINARY/OCTAL/DECIMAL/HEXADECIMAL")
print("CAN'T CONVERT THE NUMBERS IN POINT")
ans="YES"
while ans.upper()=="YES":
    print("~"*70)
    NUM=input("ENTER THE NUMBER:-")
    TYPE=input("WHICH TYPE OF NUMBER YOU ENTERED(IN ALPHABETS):-")
    if TYPE.upper()=="BINARY":
        cot=input("IN WHICH YOU WANT TO CONVERT:-")
        d = 0
        for i in NUM:
            d = d * 2 + int(i)
        if cot.upper()=="DECIMAL":
            print("DECIMAL VALUE OF", NUM, "IS:-", d)
        elif cot.upper()=="OCTAL":
            OCT = ""
            l = 0
            A = ['0', '1', '2', '3', '4', '5', '6', '7']
            while d > 0:
                l = d % 8
                OCT = A[l] + OCT
                d = d // 8
            print("OCTAL OF", NUM, "IS:-", OCT)
        else:
            hex=""
            l=0
            A=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            while d>0:
                l=d%16
                hex=A[l]+hex
                d=d//16
            print("HEXADECIMAL VALUE OF",NUM,"IS:-",hex)
    elif TYPE.upper()=="DECIMAL":
        d=int(NUM)
        cot=input("IN WHICH YOU WANT TO CONVERT:-")
        if cot.upper()=="BINARY":
            BIN=""
            s=0
            while d>0:
                s=d%2
                BIN=str(s)+BIN
                d=d//2
            print("BINARY OF",NUM,"IS:-",BIN)
        elif cot.upper()=="OCTAL":
            OCT = ""
            l = 0
            A = ['0', '1', '2', '3', '4', '5', '6', '7']
            while d > 0:
                l = d % 8
                OCT = A[l] + OCT
                d = d // 8
            print("OCTAL OF", NUM, "IS:-", OCT)
        else:
            hex = ""
            l = 0
            A = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            while d > 0:
                l = d % 16
                hex = A[l] + hex
                d = d // 16
            print("HEXADECIMAL VALUE OF", NUM, "IS:-", hex)
    elif TYPE.upper()=="OCTAL":
        cot=input("IN WHICH YOU WANT TO CONVERT:-")
        a = 0
        b = 1
        c = int(NUM)
        while c > 0:
            d = c % 10
            a += d * b
            b = b * 8
            c //= 10
        h=a
        if cot.upper()=="DECIMAL":
            print("DECIMAL VALUE OF",NUM,"IS:-",a)
        elif cot.upper()=="BINARY":
            BIN = ""
            s = 0
            while h>0:
                s=h%2
                BIN=str(s)+BIN
                h=h//2
            print("BINARY OF", NUM, "IS:-", BIN)
        else:
            hex = ""
            l = 0
            A = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            while a > 0:
                l=a%16
                hex=A[l]+hex
                a=a//16
            print("HEXADECIMAL VALUE OF", NUM, "IS:-", hex)
    else:
        cot=input("IN WHICH YOU WANT TO CONVERT:-")
        Q = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        N = len(NUM)
        d = 0
        for i in range(N):
            if NUM[i] in Q:
                d += Q[NUM[i]] * 16 ** (N - 1 - i)
            else:
                d += int(NUM[i]) * 16 ** (N - 1 - i)
        if cot.upper()=="DECIMAL":
            print("DECIMAL OF", NUM, "IS:-", d)
        if cot.upper()=="BINARY":
            BIN = ""
            H = 0
            while d> 0:
                H = d % 2
                BIN = str(H) + BIN
                d = d // 2
            print("BINARY OF", NUM, "IS:-", BIN)
        if cot.upper()=="OCTAL":
            OCT = ""
            l = 0
            A = ['0', '1', '2', '3', '4', '5', '6', '7']
            while d > 0:
                l = d % 8
                OCT = A[l] + OCT
                d = d // 8
            print("OCTAL OF", NUM, "IS:-", OCT)
    print("~"*70)
    ans=input("WANT TO CONVERT AGAIN:-")
    if ans.upper()=="NO":
        print("THANK YOU FOR VISITING")