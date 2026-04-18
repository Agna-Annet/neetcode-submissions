class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if (ord(s[left]) in range(97, 123) or ord(s[left]) in range(48, 58)) and (
                ord(s[right]) in range(97, 123) or ord(s[right]) in range(48, 58)
            ):
                if s[left] != s[right]:
                    return False
            if ord(s[left]) not in range(97, 123) and ord(s[left]) not in range(48, 58):
                left += 1
            elif ord(s[right]) not in range(97, 123) and ord(s[right]) not in range(
                48, 58
            ):
                right -= 1
            else:
                left += 1
                right -= 1
        return True 