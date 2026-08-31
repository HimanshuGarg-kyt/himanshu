n = int(input("enter N : "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    if i==1:
        print("*")
    else:
        print("*"," "*(2*i-3),"*",sep="")

for el in range(1,n):
    for el1 in range(1,el+1):
        print(" ",end = "")
    print("*",end = "")
    for el2 in range(2*(n-el)-2,1,-1):
        print(" ",end = "")  
    if el==n-1:
        print()
        continue
    print("*")