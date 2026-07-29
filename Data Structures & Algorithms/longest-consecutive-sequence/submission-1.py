class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        n = len(nums)
        for i in range(n):
            if nums[i] - 1 in num_set:
                continue
            else:
                length = 1
                while nums[i] + length in num_set:
                    length += 1
                longest = max(length, longest)
        
        return longest