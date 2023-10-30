class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for char in s:
            if char.isalnum():
                word.append(char.lower())

        start = 0
        end = len(word) - 1
        
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        
        return True