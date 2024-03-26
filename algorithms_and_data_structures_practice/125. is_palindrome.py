class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        res = ''
        for i in s:
            if i.isalnum():
                res += i
        return res == res[::-1]


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama."))
