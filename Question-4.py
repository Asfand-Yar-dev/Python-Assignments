# Q4. Fibonacci Series

# Print the first n Fibonacci numbers.

number = int(input("Enter a number:"))

fib_list = []
a=0
b=1

for i in range(number):
    fib_list.append(a)
    next_num = a+b 
    a=b
    b=next_num

print("Fibonacci series:", fib_list)

