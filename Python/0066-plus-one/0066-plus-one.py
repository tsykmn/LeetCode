class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = len(digits)
        if n == 1:
            if digits[0] < 9:
                digits[0] += 1
            else:
                digits[0] = 1
                digits.append(0)
        else:
            if digits[n-1] < 9:
                digits[n-1] += 1
                return digits
            else:
                rev_digits = digits[::-1]
                leftover = 0
                for d in range(n):
                    if rev_digits[d] == 9:
                        rev_digits[d] = 0
                        leftover = 1
                    else:
                        rev_digits[d] += 1
                        return rev_digits[::-1]
                if leftover:
                    rev_digits.append(leftover)
                return rev_digits[::-1]
        return digits
