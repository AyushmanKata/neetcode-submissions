class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occur = len(nums) / 2
        for i in nums:
            if nums.count(i) > occur:
                return i