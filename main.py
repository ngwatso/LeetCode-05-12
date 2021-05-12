class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        newList = []
        newNum = 0

        for num in nums:
                newNum += num
                newList.append(newNum)
        return newList
        
        
'''

U:

[1, 2, 3, 4, 5]
output = [1, 3, 6, 10, 15]

[2, 4, 6, 8]
output = [2, 6, 12, 20]

[1, 3, -4, -6]
output = [1, 4, 0, -6]

P:

iterate through array, add each index to previous answer

'''