def bubbleSort(arrayToSort):
    """
    Time complexity:
        best    : O(n) - when the array is already sorted
        average : O(n^2)
        worst   : O(n^2)
    parameters:
        arrayToSort : Array to be sorted
    returns:
        Sorted array
    """
    iCount = 0
    isSorted = False
    size = len(arrayToSort)
    while not isSorted:
        isSorted = True
        for i in range(0, size - iCount - 1):
            if arrayToSort[i] > arrayToSort[i + 1]:
                arrayToSort[i], arrayToSort[i + 1] = arrayToSort[i + 1], arrayToSort[i]
                isSorted = False
            print(i)
        iCount += 1
    return arrayToSort