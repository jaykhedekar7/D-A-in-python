def BubbleSort(array):
    length = len(array)
    
    for i in range(length - 1):
        for j in range(length-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array