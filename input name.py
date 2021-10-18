from colorama import Fore, Style
alpha={'A':[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1]],
       'B':[[1,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,0]],
       'C':[[0,0,1,1,1,0,0],[1,0,0,0,0,1,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,1,0],[0,0,1,1,1,0,0]],
       'D':[[1,1,1,1,1,0,0],[1,0,0,0,0,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,1,0],[1,1,1,1,1,0,0]],
       'E':[[1,1,1,1,1,1,1],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,1,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,1,1,1,1]],
       'F':[[1,1,1,1,1,1,1],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,1,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0]],
       'G':[[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,0],[1,0,0,0,1,0,0],[1,0,0,0,1,0,0],[1,1,1,1,1,0,0]],
       'H':[[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1]],
       'I':[[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[1,1,1,1,1,1,1]],
       'J':[[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[1,0,0,1,0,0,0],[0,1,1,0,0,0,0]],
       'K':[[1,0,0,0,1,0,0],[1,0,0,1,0,0,0],[1,0,1,0,0,0,0],[1,1,0,0,0,0,0],[1,0,1,0,0,0,0],[1,0,0,1,0,0,0],[1,0,0,0,1,0,0]],
       'L':[[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,1,1,1,1]],
       'M':[[1,0,0,0,0,0,1],[1,1,0,0,0,1,1],[1,0,1,0,1,0,1],[1,0,0,1,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1]],
       'N':[[1,0,0,0,0,0,1],[1,1,0,0,0,0,1],[1,0,1,0,0,0,1],[1,0,0,1,0,0,1],[1,0,0,0,1,0,1],[1,0,0,0,0,1,1],[1,0,0,0,0,0,1]],
       'O':[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,1,1,1,1,1,0]],
       'P':[[1,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0]],
       'Q':[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,1,1,1,1,1,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0]],
       'R':[[1,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1]],
       'S':[[0,1,1,1,1,1,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,1,1,1,1,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,1,1,1,1,1,0]],
       'T':[[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]],
       'U':[[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,1,1,1,1,1,0]],
       'V':[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,1],[0,1,0,0,0,1,0],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0]],
       'W':[[1,1,0,0,0,1,1],[0,1,0,0,0,1,0],[0,1,0,0,0,1,0],[0,1,0,1,0,1,0],[0,1,0,1,0,1,0],[0,1,0,1,0,1,0],[0,0,1,0,1,0,0]],
       'X':[[1,0,0,0,0,0,1],[0,1,0,0,0,1,0],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]],
       'Y':[[1,0,0,0,0,0,1],[0,1,0,0,0,1,0],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]],
       'Z':[[1,1,1,1,1,1,1],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,1,0,0,0],[0,0,1,0,0,0,0],[0,1,0,0,0,0,0],[1,1,1,1,1,1,1]],
       ' ':[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],
       }
while True:
    name = input("enter your name : ")
    c= input("ENTER IN WHICH COLOR YOU WANT TO PRINT THE INPUT PROVIDED (MAGENTA/CYAN/GREEN/RED/YELLOW/BLUE/BLACK) : ")
    L = ''
    fn =[[0],[0],[0],[0],[0],[0],[0]]
    for ch in name.upper():
        L = alpha[ch]
        for i in range(7):
            fn[i] = fn[i]+[0]+L[i]
    for i in range(7):
        for j in range(len(fn[i])):
            if fn[i][j] == 1:
                if c.upper() == "MAGENTA":
                    print(Fore.MAGENTA + "*"+ Style.RESET_ALL, end='')
                elif c.upper() == "CYAN":
                    print(Fore.CYAN + "*"+ Style.RESET_ALL, end='')
                elif c.upper() == "GREEN":
                    print(Fore.GREEN + "*"+ Style.RESET_ALL, end='')
                elif c.upper() == "RED":
                    print(Fore.RED + "*"+ Style.RESET_ALL, end='')
                elif c.upper() == "YELLOW":
                    print(Fore.YELLOW + "*"+ Style.RESET_ALL, end='')
                elif c.upper() == "BLUE":
                    print(Fore.BLUE + "*"+ Style.RESET_ALL, end='')
                elif c.upper() == "BLACK":
                    print(Fore.BLACK + "*"+ Style.RESET_ALL, end='')
            else:
                print("", end=' ')
        print()
    do=input("WANT TO PRINT AGAIN (YES/NO):-")
    if do.upper()=="YES":
        pass
    else:
        break