class Solution:
    def isValid(self, s: str) -> bool:
        
        characters = {'(':')', '{':'}', '[':']'}
        stack = []

        for char in s:
            if char in characters:
                stack.append(char)
            elif stack and char == characters[stack.pop()]:
                continue
            else:
                return False

        return True if len(stack) == 0 else False