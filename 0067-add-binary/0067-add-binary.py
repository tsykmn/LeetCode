class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        s = []
        while i>= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2
        return ''.join(reversed(s))