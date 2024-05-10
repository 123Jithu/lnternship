n = int(input("Enter the number:"))

def factorial(n): 
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * factorial(n - 1)) 

print("number:", n)
print("Factorial:", factorial(n))

