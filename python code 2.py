#Python program to find the factorial of a number provided by the user.
E
num = int(input("Enter the number to do the factorial function:"))
factorial = 1
if (num<0):
print("Sorry no factorial value for negative numbers")
elif (num>0):
for i in range(1,num + 1):
factorial = factorial*i
print("The factorial of", num, "is", factorial)
elif (num==0):
print("The factorial of 0 is 1")
