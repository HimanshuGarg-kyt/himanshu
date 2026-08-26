password = "08062008"

for i in range(3):
    a = input("enter password : ")
    if a == password:
        print("ACCESS GRANTED")
        exit()
else:
    print("ACCESS DENIED")  
