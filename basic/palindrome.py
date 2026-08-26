a = input("enter : ")
b = a.upper()
c=b.replace(" ","")
i = len(c)-1
j = 0
while i>j:
    if c[i]==c[j]:
        i-=1
        j+=1
        continue
    else:
        print("NOT PALINDROME")
        break
else:
    print("PALINDROME")
