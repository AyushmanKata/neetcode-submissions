class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) % 2 == 0:
                continue
            else:
                return False
        return True