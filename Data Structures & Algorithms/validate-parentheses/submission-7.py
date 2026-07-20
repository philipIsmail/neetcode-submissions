class Solution:
    def isValid(self, s: str) -> bool:
        
        characters = {'(':')', '{':'}', '[':']'}
        stack = []

        for char in s:
            if char in characters:
                stack.append(char)
                print(stack)
            elif stack and char == characters[stack[-1]]:
                stack.pop()
            else:
                return False

        return True if len(stack) == 0 else False