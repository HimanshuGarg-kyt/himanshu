balance = 10000
while balance >= 0:
    print("1.Check balance\n2.Deposit\n3.Withdraw\n4.Exit")
    a = int(input("enter option number : "))
    if a > 4 or a < 1:
        continue
    if a == 1:
        print("your balance is : ", balance)
    elif a == 2:
        deposit = int(input("enter your deposit amount : "))
        if deposit >= 0:
            balance += deposit
        else:
            print("error")
    elif a == 3:
        withdraw = int(input("enter the amount which you want to withdraw : "))
        if withdraw <= 0:
            print("error")
        elif withdraw > balance:
            print("balance is not sufficient")
        else:
            balance -= withdraw
    elif a == 4:
        break
    