# fibonnaci series

limit = int(input('enter the limit :'))
a, b = 0, 1

print(a, b, end=" ")
for x in range(2, limit):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

