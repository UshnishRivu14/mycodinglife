arr = [20,9,16,3,5]
n = len(arr)

print("Array before sort: ")
print(arr)
for i in range(1,n):
    temp = arr[i]
    j = i - 1
    while(j >= 0 and temp < arr[j]):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = temp

print('Array after sorting')
print(arr)
