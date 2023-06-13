arr = [1,9,3,6,2,8]
n = len(arr)

print("arrray before sorting: ")
print(arr)

for i in range(n-1):
    pos_smallest = i
    for j in range(i+1, n):
        if  arr[j] < arr[pos_smallest]:
            pos_smallest = j

    arr[i], arr[pos_smallest] = arr[pos_smallest], arr[i]

print('Array after sorting')
print(arr)
