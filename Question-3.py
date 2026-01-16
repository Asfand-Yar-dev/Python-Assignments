# Q3: Print All Primes in Range

# Take an input n and print all prime numbers from 1 to n.
# The function should return the prime numbers as a list.

number = int(input("Enter a number:"))

def check_isprime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
#TODO
# should be in function of below
prime_list = []
for num in range(1,number+1):
    if check_isprime(num):
        prime_list.append(num)

print("Prime numbers are:", prime_list)