class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = Counter(ransomNote)
        m = Counter(magazine)

        for rKey in r.keys():
            if not rKey in m.keys() or m[rKey] < r[rKey]:
                return False
        return True