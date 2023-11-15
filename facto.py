def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


input1 = int(input("Enter the number : "))
print("The Factorial of the given number is :  ", fact(input1))
