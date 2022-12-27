# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....

def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

number = int(input("Enter a number-->"))
print(fibonacci(number))