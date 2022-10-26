# Different ways to clear a list.
# case 1:- using clear()

lis = list(input('enter the elements of list :').split())
print("list before clearing :", lis)
lis.clear()
print("list after clearing :", lis)

# case 2:- using del

lis1 = list(input('enter the elements of list1 :').split())
print("list before clearing :", lis1)
del lis1[:]
print("list after clearing :", lis1)

# case 3:- using reinitialization

lis2 = list(input('enter the elements of list2 :').split())
print("list before clearing :", lis2)
lis2 = []
print("list after clearing :", lis2)

# case 4:- using *=0

lis3 = list(input('enter the elements of list3 :').split())
print("list before clearing :", lis3)
lis3 *= 0
print("list after clearing :", lis3)

