# Python program to count Even and Odd numbers in a List

#taking list elements from the user and printing
lis = list(map(int, input("enter the list element :").split()))
print("the actual list is :", lis)

#taking two variables for finding the odd and even number count
count_even, count_odd = 0, 0

#using loop take elements from the list and checking the reminder is 0 or not when it devided by 2
for elem in lis:
    if (elem % 2) == 0:
        # if it is zero incerementing the even count by one
        count_even = count_even + 1
    else:
        #if it is not zero then incrementing the odd count bye one 
        count_odd = count_odd + 1

#printing the total count of even and odd number from the given list        
print("count of even numbers in list :", count_even)
print("count of odd numbers in list :", count_odd)

