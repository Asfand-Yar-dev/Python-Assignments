# Q2: Prime Number Check

# Input a number and check if it is prime.
# This should be coded as a function. Return True if prime, return False if not.
p=input("Enter a number: ")
def prime_number(p):
    
    if p<=1:
        return False
    for i in range(2,p):
        if p%i==0:
            return False
    return True

print("Prime numbers are:", prime_number(int(p)))


