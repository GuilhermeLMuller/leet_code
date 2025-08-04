class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        palindrome = True
        index = 0
        for i in reversed(x):
            if i != x[index]:
                palindrome = False
            index = index + 1
        return palindrome
