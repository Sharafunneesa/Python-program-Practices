# Python program to find the smallest number in a list

#taking list elements from user and printing
lis = list(map(int, input("enter the list element :").split()))
print(lis)

#printing the smallest number in list using builtin function min
print("the smallest is :", min(lis))

#for finding the smallest number in the list without using builtin function
#consider the first element in the list is small and assign into variable name small
small = int(lis[0])

#using for loop taking elements in list one by one and checking with small 
#if the next element less than that of small the small will uodate with new small numbe
for i in lis:
    if small >= int(i):
        small = int(i)

#printing the smallest value in the list
print("the smallest number in list :", small)
