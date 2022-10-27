# Python program to print all odd numbers in a range

ran = int(input("enter the range :"))
print("odd numbers in given range are : ", end="")
for i in range(0, ran + 1):
    if (i % 2) != 0:
        print(i, end=" ")