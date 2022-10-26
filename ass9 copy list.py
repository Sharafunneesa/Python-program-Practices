# python program to copy a list
# case 1 :-

lis = list(input('enter list elements :').split())
num = []
for i in lis:
    num.append(i)
print("copied list :", num)

# case 2 :-

num = lis.copy()
print("copied list :", num)


