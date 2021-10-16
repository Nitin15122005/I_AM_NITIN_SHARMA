n ="YES"
while n.upper() == "YES":
       print("~" * 50)
       print("What You Want To Do ??")
       print("Enter 1:-To Get ASCII Of a String")
       print("Enter 2:-To Get String From ASCII")
       print("~" * 50)
       choice=int(input("Enter your choice:-"))
       if choice== 1:
              name = input("Enter The String:- : ")
              asc = {"A": 1000001,"B": 1000010,"C": 1000011,"D": 1000100,"E": 1000101,"F": 1000110,"G": 1000111,"H": 1001000,"I": 1001001,"J": 1001010,"K": 1001011,"L": 1001100,"M": 1001101,"N": 1001110,"O": 1001111,"P": 1010000,"Q": 1010001,"R": 1010010,"S": 1010011,"T": 1010100,"U": 1010101,"V": 1010110,"W": 1010111,"X": 1011000,"Y": 1011001,"Z": 1011010}
              for ch in name.upper():
                     print(asc[ch],end=' ')
       elif choice == 2:
              STRING={"1000001":"A","1000010":"B","1000011":"C","1000100":"D","1000101":"E","1000110":"F","1000111":"G","1001000":"H","1001001":"I","1001010":"J","1001011":"K","1001100":"L","1001101":"M","1001110":"N","1001111":"O","1010000":"P","1010001":"Q","1010010":"R","1010011":"S","1010100":"T","1010101":"U","1010110":"V","1010111":"W","1011000":"X","1011001":"Y","1011010":"Z"}
              a = input("Enter the string:-")
              s= a.split(" ")
              for i in range(len(s)):
                     print(STRING[s[i]],end=" ")
       else:
              print("INVALID INPUT PROVIDED")
       n = input("\nWANT GO AGAIN (YES/NO) : ")
else:
       print("THANKS FOR USING THIS PROGRAM.🎮")