class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = ''
        
        for stri in strs:
            enc_string += str(len(stri)) + "?" + stri
        
        return enc_string

    def decode(self, s: str) -> List[str]:
        list_strings = []
        ind = 0

        while ind < len(s):
            j = ind
            while s[j] != '?':
                j += 1
            length = int(s[ind:j])
            list_strings.append(s[j+1 : j+1+length])
            ind = j + 1 + length

        return list_strings

