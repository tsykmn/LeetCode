class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # make a set seen that adds characters that were already read
        # if char in seen, duplicated char + needs to be removed from substring
        # remove the previous characters from substring
        # otherwise, add it to seen + adjust substring

        # pointers
        # left pointers at start and moves to right when duplicated char is seen
        # right continues moving regardless
        # left is used to adjust the substring when it was duplicated

        seen = set()
        n = len(s)
        left = 0

        result = 0

        for right in range(n):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[right])

            result = max(len(seen), result)
        
        return result