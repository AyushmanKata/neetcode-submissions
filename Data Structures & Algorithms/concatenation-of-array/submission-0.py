class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in nums:
            result.append(i)
        ans = 2*result
        return ans   