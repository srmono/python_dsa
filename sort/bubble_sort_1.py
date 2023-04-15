def bubbleSort(arrayToSort):
    """
    Time complexity:
        best    : O(n^2)
        average : O(n^2)
        worst   : O(n^2)
    parameters:
        arrayToSort : Array to be sorted
    returns:
        Sorted array
    """
    size = len(arrayToSort)
    for i in range(size):
        for j in range(0, size - i - 1):
            if arrayToSort[j] > arrayToSort[j + 1]:
                arrayToSort[j], arrayToSort[j + 1] = arrayToSort[j + 1], arrayToSort[j]
            print(i, j)
    return arrayToSort