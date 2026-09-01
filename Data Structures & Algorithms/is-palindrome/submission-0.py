class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for char in s:
            if char.isalnum():
                clean += char.lower()

        t = ""

        for i in range(len(clean) - 1, -1, -1):
            t += clean[i]

        if clean == t:
            return True
        else:
            return False

        