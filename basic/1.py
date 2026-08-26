
tupple = (1,4,9,16,25,36,49,64,81,100)
i = 0
a = int(input("enter number which you want to search :"))

while i<=9:
   c = tupple[i]
   i+=1
   if(a==c):
      print(c)
      print("number found")
      break
else:
   print("number not found")

print("hello world")

