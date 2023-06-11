arr=[12,4,34,54,34,2,33]
print("Enter the elements of array: ")
print("Array before : ")
print(arr)
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if(arr[j]>arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print("Array after sort: ")
print(arr)            