#Solution – 1 – Brute Force Method
# Time Complexity = O(n^2)
def twoNumberSum(array, targetSum):
    result = []
    for i in range(0, len(array),1):
        for j in range(i+1, len(array), 1):
            if array[i] + array[j] == targetSum:
                result.append(array[i])
                result.append(array[j])
                break
        if result != []:
            break
    return result