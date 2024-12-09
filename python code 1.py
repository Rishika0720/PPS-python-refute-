#Greater of three numbers
def largestnum(a,b,c):
if (a>b) and (a>c):
print("A is the greatest number")
elif(b>a) and (b>c):
print("B is the greatest number")
elif(c>a) and (c>b):
print("C is the greatest number")
else:
print("All are equal")
def main():
n=int(input("Enter the number 1:"))
o=int(input("Enter the number 2:"))
p=int(input("Enter the number 3:"))
largestnum(n,o,p)
main()