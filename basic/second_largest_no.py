def second_largest(nums):
    largest = second = float('-inf')
    
    for num in nums:
        if num > largest:
            # Update both largest and second largest
            second = largest
            largest = num
        elif num > second and num != largest:
            # Update second largest only if distinct
            second = num
    
    return second if second != float('-inf') else None

# Example
numbers = [10, 25, 8, 25, 17]
result = second_largest(numbers)
if result is not None:
    print("Second largest =", result)
else:
    print("No second largest found")

