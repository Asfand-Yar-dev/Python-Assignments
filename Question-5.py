# Q5. Second Largest Number

# Find the second largest number in a list.
# Code it as a function. The input would be a list of functions. Find the second largest number in that list.

def largest_list(number):
    first = float('-inf')
    second = float('-inf')
    for num in number:
        if num > first:
            second=first
            first=num
        elif num > second and num!=first:
            second=num
    return second
number = [1,1,1]
print("Second largest number is:", largest_list(number))
