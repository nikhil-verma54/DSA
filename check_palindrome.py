class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        original = x

        reverse = 0
        while x>0:
            y = x%10
            reverse = reverse*10 +y
            x = x//10
        if original == reverse:
            return True
        else:
           return False
sol = Solution()
x = 1221
print(sol.isPalindrome(x))  