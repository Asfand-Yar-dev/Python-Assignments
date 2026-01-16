# Q7. Count Digits

# Input a number and count how many digits it has.

# Example: 12345 → 5 (The input of the function should be an integer)

n=int(input("Enter a number:"))

def len_number(n):
    len_count = 0
    number = n
    while number > 0:
        len_count = len_count+1
        number = number//10
    return len_count

print(len_number(n))

# floor division concept