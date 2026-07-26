class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        output = True
        s_dict = {}

        # O(n)
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        
        # O(n)
        if len(s) == len(t):
            for letter in t:
                if letter in s_dict and s_dict[letter] > 0:
                    s_dict[letter] -= 1
                else: 
                    output = False
                    break
        else:
            output = False
        
        return output