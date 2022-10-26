# minimum of two numbers.

num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))
print("numbers are :", num1, num2)
print("the minimum number is :", end=" ")
if num1 < num2:
    print(num1)
else:
    print(num2)