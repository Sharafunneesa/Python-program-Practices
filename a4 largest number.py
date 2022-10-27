# Python program to find the largest number in a list

lis = list(map(int, input("enter the list element :").split()))
print(lis)
print("the largest is :", max(lis))
large = int(lis[0])
for i in lis:
    if large <= int(i):
        large = int(i)
print("the largest number in list :", large)



