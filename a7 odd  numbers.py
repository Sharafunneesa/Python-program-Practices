# Python program to print odd numbers in a List

lis = list(map(int, input("enter the list element :").split()))
print("the actual list is :", lis)
print("odd numbers in list is :", end=" ")
for elem in lis:
    if (elem % 2) != 0:
        print(elem, end=" ")