class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alph = {'a':0, 'e':0, 'o':0, 'u':0}
        n = len(sentence)
        for i in range(n):
            if sentence[i] in alph:
                alph[sentence[i]] += 1
        return min(alph.values()) == 1