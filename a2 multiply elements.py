# Python Multiply all numbers in the list

lis = list(input("enter the elements :").split())
print("the input list is :", lis)
mul = 1
for elem in lis:
    mul = mul * int(elem)
print("the multiply of all numbers in list is :", mul)
