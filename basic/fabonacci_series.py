n = int(input("enter number : "))
a = 0
b = 1
i = 0
while i<n:
    print(a)
    print(b)
    a += b
    b += a
    i+=2