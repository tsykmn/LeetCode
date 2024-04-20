class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)
        for i in range(n):
            if digits[n-i-1] < 9:
                digits[n-i-1] = digits[n-i-1] + 1
                return digits
            digits[n-i-1] = 0
        arr = [0]*(n+1)
        arr[0] = 1
        digits = arr
        return digits
        
        # dummy attempt
        # n = len(digits)
        # last = digits[n-1] + 1
        # reverse = [0]*n
        # if last > 10:
        #     for i in range(n):
        #         current = digits[n-i-1] + 1
        #         if current >= 10:
        #             reverse.append(0)
        #             reverse.append(1)
        #             digits[n-i-2] = digits[n-i-2] + 1
        #         else:
        #             reverse.append(current)
        # else:
        #     digits[n-1] = last
        #     return digits
        # return reverse


