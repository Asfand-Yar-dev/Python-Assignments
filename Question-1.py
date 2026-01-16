# Q1: Simple Password Validator

#Password must:
#be at least 8 characters
#contain a digit
#contain an uppercase letter
#This should be coded as a function, where we give the password as input and the function should return True/False based on of the password is a valid password or not. 
#The function should also print a message stating the reason why the password is not valid in case it is invalid.

def password_valid(n):
    if len(n)<8:
        print("Password should be 8 characters long")
        return False
    
    has_digit = False
    has_upper = False
    for ch in n:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
        
    if not has_digit:
            print("Password should contain at least one digit")
            return False
        
    if not has_upper:
            print("Password should contain at least one uppercase letter")
            return False
        
    return True

print(password_valid("Asfandyar1"))
print(password_valid("asfandyar"))
print(password_valid("Asfandyar"))
print(password_valid("asfandyar1"))
print(password_valid("yar"))

        