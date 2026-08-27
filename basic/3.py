# def sum_n(number):
#     if number ==0:
#         return 0
#     elif number<0:
#         return "error"
#     else:
#         return number+sum_n(number-1)

# n = int(input())
# print(sum_n(n))

def sum_n(number: int) -> int:
    if number < 0:
        raise ValueError("Number must be non-negative.")
    if number == 0:
        return 0
    return number + sum_n(number - 1)


try:
    n = int(input("Enter a non-negative integer: "))
    print(sum_n(n))
except ValueError as e:
    print(f"Invalid input: {e}")