def VowCount():
    cnt = 0
    str1 = input("Enter a string: ")
    word = str1.split()
    for i in word:
        if i[0] in 'aeiouAEIOU':
            cnt += 1
            print(i)
    print("Vowel words:",cnt)

VowCount()