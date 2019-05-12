def SelectionSort(array):
    length = len(array)
    for i in range(length): 
        min_idx = i 
        for j in range(i+1, length): 
            if array[min_idx] > array[j]: 
                min_idx = j 
                      
        array[i], array[min_idx] = array[min_idx], array[i] 

    return array       