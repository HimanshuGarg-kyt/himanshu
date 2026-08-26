a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("Binary of a:", bin(a))
print("Binary of b:", bin(b))

print("AND:", a & b, bin(a & b))
print("OR:", a | b, bin(a | b))
print("XOR:", a ^ b, bin(a ^ b))
print("NOT a:", ~a, bin(~a))
print("NOT b:", ~b, bin(~a))
print("Left shift a:", a << 1, bin(a << 1))
print("Right shift b:", b >> 1, bin(b >> 1))
