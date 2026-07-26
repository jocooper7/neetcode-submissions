class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n) space complexity where n is the number of strings in strs and each string has its own key
        result = defaultdict(list)

        # O(n) where n is the number of strings in strs
        for stri in strs:
            count = [0] * 26

            # O(m) where m is the number of letters in the longest string
            for char in stri:
                count[ord(char) - ord('a')] += 1

            result[tuple(count)].append(stri)

        return list(result.values())

        # Total time complexity of O(n*m)