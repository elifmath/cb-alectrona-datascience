def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact 

number=int(input("Please enter a number : "))
result=factorial(number)

print("The factorial result is :" , (result))
