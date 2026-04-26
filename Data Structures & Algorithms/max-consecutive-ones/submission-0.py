class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        my_list = []
        count = 0
        for i in nums:
            if i == 0:
                count = 0
            else:
                count += 1
            my_list.append(count)
        return max(my_list)
        
        
                