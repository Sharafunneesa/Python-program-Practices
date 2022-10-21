# finding the given number is palindrome number or not

num = int(input('enter the number :'))

if num < 0:
    print('the number is invalid')
else:
    sum = 0

temp = num

while num > 0:
    rem = num % 10
    sum = (sum * 10) + rem
    num = num // 10

if sum == temp:
    print('the given number is palindrome number')
else:
    print('the given number is not palindrome number')


