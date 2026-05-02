class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for num in sorted(arr)[::-1]:
            if arr.count(num) == num:
                return num
        return -1