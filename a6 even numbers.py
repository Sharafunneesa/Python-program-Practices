# Python program to print even numbers in a list

#taking the element of list from the user and printing the actual list
lis = list(map(int, input("enter the list element :").split()))
print("the actual list is :", lis)
print("even numbers in list is :", end=" ")

#using for loop take one by one element in the list and divided with two
#if the reminder is 0 then it printing
for elem in lis:
    if (elem % 2) == 0:
        print(elem, end=" ")
