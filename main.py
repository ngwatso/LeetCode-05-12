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

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        res = []

        for i in candies:
            k = i + extraCandies
            for index, j in enumerate(candies):
                if k >= j and index == len(candies) - 1:
                    res.append(True)
                elif k >= j:
                    continue
                else:
                    res.append(False)
                    break
        return res

# ========================================

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])

        return res
            
    
        
        
        
'''

U:

[1, 2, 3, 4, 5, 6]
n = 3
output = [1, 4, 2, 5, 3, 6]

[5, 2, 6, 7]
n = 2
output = [5, 6, 2, 7]

P:

create 2 lists called res_1 & res_2, create int called count. iterate through nums, appending to res based on count

'''