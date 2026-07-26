class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        output = False

        for i in nums:
            if i in nums_dict:
                output = True
                break
            else:
                nums_dict[i] = 1

        return output
