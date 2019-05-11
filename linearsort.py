def linearSort(arr, target):
    length = len(arr)
    for value in range(length):
        if arr[value] == target:
            print("Value found in position: ", value)
        else:
            print("Not found")
            
