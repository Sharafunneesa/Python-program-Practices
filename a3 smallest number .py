# Python program to find the smallest number in a list

lis = list(map(int, input("enter the list element :").split()))
print(lis)
print("the smallest is :", min(lis))

small = int(lis[0])
for i in lis:
    if small >= int(i):
        small = int(i)
print("the smallest number in list :", small)
