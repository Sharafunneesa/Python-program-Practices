# Python program to find second-largest number in a list

lis = list(map(int, input("enter the list element :").split()))
print(lis)
large = (lis[0])
second_large = 0
for i in lis:
    if large <= int(i):
        second_large = large
        large = int(i)
    elif int(i) != large and second_large <= int(i):
        second_large = int(i)
print("the second largest number is :", second_large)

