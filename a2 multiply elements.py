# Python Multiply all numbers in the list

#taking the element of list fro user and printing it
lis = list(input("enter the elements :").split())
print("the input list is :", lis)

#taking one variable name mul and initializing with one 
mul = 1

#using for loop taking elements from list one by one and mltiply with mul and store in mul
for elem in lis:
    mul = mul * int(elem)

#printing the total multiply value     
print("the multiply of all numbers in list is :", mul)
