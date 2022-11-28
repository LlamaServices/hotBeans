class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        lenght = len(s)
        left = 0
        right = lenght - 1
        half = lenght // 2
        while left <= half:
            if s[left] != s[right]:
                return False
            left  += 1
            right -= 1

        return True