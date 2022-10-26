# swapping of two elements

lis = list((input('enter the elements :').split()))
pos1 = int(input('enter the position to be swap:'))
pos2 = int(input('enter the position to be swap:'))
print("list before swap :", lis)
lis[pos1], lis[pos2] = lis[pos2], lis[pos1]
print("list after swap :", lis)
