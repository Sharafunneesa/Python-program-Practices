# Python program to count Even and Odd numbers in a List

lis = list(map(int, input("enter the list element :").split()))
print("the actual list is :", lis)
count_even, count_odd = 0, 0
for elem in lis:
    if (elem % 2) == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
print("count of even numbers in list :", count_even)
print("count of odd numbers in list :", count_odd)

