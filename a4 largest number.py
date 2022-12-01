# Python program to find the largest number in a list

#taking list elements from user and printing it 
lis = list(map(int, input("enter the list element :").split()))
print(lis)

#printing the largest element in the list using in built function
print("the largest is :", max(lis))

#for finding the largest number in the list without using in build function
#consider the first element in the list is largest number and assign to the variable large
large = int(lis[0])

#using for loop taking elemnts fron user one bye one and checking with large 
#if it greater than large then large will uodated with new value
for i in lis:
    if large <= int(i):
        large = int(i)

#printing the large number from the list        
print("the largest number in list :", large)



