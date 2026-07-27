class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(2n) space complexity where n is the number of numbers in nums
        count_dict = {}
        freq_arr = [[] for index in range(len(nums) + 1)]

        # O(n) time complexity where n is the number of numbers in nums
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)

        # O(n) time complexity where n is the number of numbers in nums
        for num, cou in count_dict.items():
            freq_arr[cou].append(num)

        # O(n) space complexity where n is the number of numbers in nums
        result = []
        # O(n) time complexity where n is the number of numbers in nums
        for i in range(len(freq_arr) - 1, 0, - 1):
            for num in freq_arr[i]:
                result.append(num)
                if len(result) == k:
                    return result

        # Simplified time complexity is O(n) and space complexity is O(n)