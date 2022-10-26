# python program to reverse a list
# case 1 :-

lis = list(input('enter elements of list :').split())
print('actual list :', lis)
lis1 = []
for i in lis:
    lis1.insert(0, i)
print("the reversed list :", lis1)

# case 2 :-

lis.reverse()
print('the reversed list :', lis)
