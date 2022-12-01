# Python Sum of number digits in List
#taking the list element from user
lis = list(input("enter the elements :").split())
print("the input list is :", lis)

#taking an empty list for saving output
out = []

#usin for loop to get the element from list one by one
for elem in lis:
    sum = 0
    #using for loop adding digits of one element and uppending into output list
    for digit in str(elem):
        sum = sum + int(digit)
    out.append(sum)
#printing the output list
 print("the output list is :", out)
