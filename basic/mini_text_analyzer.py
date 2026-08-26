a = input("enter a sentence : ")

print("Number of characters: ", len(a))

b = ""
for el in a:
    if el.isalpha():
        b+=el

i=0
c = "aeiouAEIOU"
for el in b:
    if el in c:
        i+=1
print("Number of vowels: ",i)

print("Number of consonant: ",len(b)-i)

j = 0 
for el in a:
    if el.isdigit():
        j+=1
print("Number of digit : ",j)

k = 0
for el in a:
    if el.isspace():
        k+=1
print("Number of spaces: ",k)

print("Number of words : ",k+1)