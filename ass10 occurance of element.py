# count occurrence of an element in a list
# case 1:-

lis = list(input("enter the elements of list :").split())
elem = input("enter the element to check :")
count1 = 0
for i in lis:
    if i == elem:
        count1 = count1 + 1
print("the occurrence of element in list is :", count1)

# case 2:-

count = lis.count(elem)
print("the occurrence of element in list is :", count)

