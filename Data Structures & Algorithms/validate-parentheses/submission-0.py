class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dict = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in paren_dict:
                if stack and stack[-1] == paren_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False