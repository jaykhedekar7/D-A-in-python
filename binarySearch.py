def BinarySearch(target, array):
    low = 0
    high = len(array)-1
    #binary search needs sorted array only
    #Used the function sorted instead of method list.sort since the function returns an iterable list
    sortArray = sorted(array)

    while low <=high:
        #// dumps the decimal part of the quotient
        middle = (high+low)//2

        if sortArray[middle] == target:
            print("Value found at", middle)
            return True

        elif target < sortArray[middle]:
            high = middle - 1

        else:
            low= middle + 1

    print("Value not found")
    return False 



