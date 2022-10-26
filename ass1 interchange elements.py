# python program to interchange to first and last elements.

lis = list((input("enter the element :").split()))
print("the actual list is :", lis)

lis[0], lis[-1] = lis[-1], lis[0]
print("interchanged list is :", lis)




