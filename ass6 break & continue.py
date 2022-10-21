# example for break and continue
count, y = 0, 1
while 1:
    if(y % 2) == 0:
        print(y, end=" ")
        if count >= 18:
            break
    count = count + 1
    y = y + 1

print(' ')
for x in range(20):
    if (x % 2) == 0:
        continue
    print(x, end=" ")
