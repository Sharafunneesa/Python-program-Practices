num = int(input('enter the number :'))

if num > 0:
    sum = 0
    temp = num
    digit = 0
else:
    print('enter invalided number')

while num > 0:
    digit = digit + 1
    num = num // 10

num = temp

while num > 0:
    rem = num % 10
    sum = sum + (rem ** digit)
    num //= 10

if sum == temp:
    print('the given number is an armstrong number')
else:
    print('the given number is not an armstrong number')
