# Python Sum of number digits in List

lis = list(input("enter the elements :").split())
print("the input list is :", lis)
out = []
for elem in lis:
    sum = 0
    for digit in str(elem):
        sum = sum + int(digit)
    out.append(sum)
print("the output list is :", out)
