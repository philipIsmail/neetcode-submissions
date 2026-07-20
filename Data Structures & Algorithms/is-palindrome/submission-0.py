class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        reverse = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                if s[i].isupper():
                    reverse += s[i].lower()
                else:
                    reverse += s[i]
        return reverse == reverse[::-1]