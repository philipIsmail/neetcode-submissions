class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {"(":")", "[":"]", "{":"}"}
        stack = []

        for c in s:

            if c in hashmap:
                stack.append(c)
            elif stack and c == hashmap[stack.pop()]:
                continue
            else:
                return False

        return len(stack) == 0
