# Q6. Reverse a Number

# Input a number and print its reverse.

# Example: 123 → 321 (The input of the function should be an integer)

n = int(input("Enter a number:"))

def reverse_number(n):
    rev = 0
    number = n
    while number >0:
        digit = number%10
        rev = rev*10+digit
        number = number//10
    return rev

print(reverse_number(n))

# TODO
#difference between single / and double //


