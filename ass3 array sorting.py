# array sorting without using inbuilt function

arr = list(map(int, input("Enter elements of array :"). split()))
print("actual array is :", arr)
new_arr = []

while arr:
    minimum = arr[0]
    for x in arr:
        if x < minimum:
            minimum = x
    new_arr.append(minimum)
    arr.remove(minimum)
print('the sorted array is :', new_arr)







