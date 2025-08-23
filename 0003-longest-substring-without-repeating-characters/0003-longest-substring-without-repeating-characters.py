class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        longest = 0
        n = len(s)
        left = 0

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[right])
                left += 1
            seen.add(s[right])
            longest = max(longest, len(seen))
        return longest


        