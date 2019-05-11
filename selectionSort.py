def SelectionSort(array):
    length = len(array)

    for i in range(length-1):
        small = array[i]

        for j in range[i+1, length-1]:
            if array[small] > array[j]:
                array[small], array[j] = array[j], array[small]