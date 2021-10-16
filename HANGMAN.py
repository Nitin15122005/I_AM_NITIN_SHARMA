import time
import random
movies=["DIL BECHARA","RADHE","SARDAAR DA GRANDSON","URI","ASPIRANTS"]
HINT=["Both Actors have cancer","Salman khan new film","JOHN ABRAHAM NEW FILM","INDIAS SURGICAL STRIKE","HOLLYWOOD"]
m=random.randint(0,4)
movie=movies[m]
print("HINT",HINT[m])
guess=[' ']
h="HANGMAN"
while True:
    print("#"*20)
    print("\t",h)
    print("#"*20)
    dash=False
    for ch in movie:
        if ch in guess:
            print(ch,end=' ')
        else:
            print("_",end=' ')
            dash=True
    if dash==False:
        print("YOU WIN!!!!!")
        break
    print()
    print("#"*20)
    g=input("ENTER THE GUESS ALPHABET:-")
    if len(g)!=1:
        print("PLEASE ENTER SINGLE ALPHABET ONLY")
        continue
    if not g.isalpha():
        print("NO SYMBOL,DIGIT OR SPACE IS ACCEPTABLE")
        continue
    g=g.upper()
    if g not in movie:
        h=h[:len(h)-1]
        if len(h)==0:
            print("YOU LOOSE,GAME OVER!!!!")
            break
    guess.append(g)
    time.sleep(0.5)