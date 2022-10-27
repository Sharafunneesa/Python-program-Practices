# Python program to print even numbers in a list

lis = list(map(int, input("enter the list element :").split()))
print("the actual list is :", lis)
print("even numbers in list is :", end=" ")
for elem in lis:
    if (elem % 2) == 0:
        print(elem, end=" ")
