a = int(input("enter a number : "))
i = 2

for el in range(2,a+1):
    b = el**0.5
    for c in range(2,int(b)+1):
        if el%c==0:
            break
    else:
        print(el)

        
