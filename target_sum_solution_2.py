# Solution – 2 [Better Solution]
# Time Complexity = O(n)
def twoNumberSum(array, targetSum):
    for iNum in array:
        expectedNum = targetSum - iNum
        if (expectedNum in array) and (expectedNum is not iNum):
            return [iNum, expectedNum]
    return []

print(twoNumberSum([1,2,3,4,8], 11) )