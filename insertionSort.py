def InsertionSort(array):
    length = len(array)
    hand = array[0]
    
    for i in range(length):
        for j in range (i, length):
            if array[j+1] > array[j]:
                