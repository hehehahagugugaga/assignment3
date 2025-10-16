def factorial(num):
    for i in range(1,num):
        num=num*i
    return num
num= int(input("Enter a number : "))
print("Factorial of ",num," is : ",factorial(num))
