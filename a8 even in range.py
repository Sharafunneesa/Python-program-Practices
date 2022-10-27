# Python program to print all even numbers in a range

ran = int(input("enter the range :"))
print("even numbers in given range are : ", end="")
for i in range(0, ran + 1):
    if (i % 2) == 0:
        print(i, end=" ")