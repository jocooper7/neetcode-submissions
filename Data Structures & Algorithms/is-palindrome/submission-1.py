class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(1) constance space complexity
        left = 0
        right = len(s) - 1

        # O(n/2) time complexity where n is the number of characters in the given string, simplified is O(n)
        while left < right:
            while left < right and not (s[left].isalnum()):
                left += 1
            while left < right and not (s[right].isalnum()):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False  

            left += 1
            right -= 1

        return True 