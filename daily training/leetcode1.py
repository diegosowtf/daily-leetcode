class Solution(object):
    def mergeAlternately(self, word1, word2):
        wordn1 = list(word1)
        for i, valor in enumerate(word2):
            wordn1.insert(i * 2 + 1, valor)
        return "".join(wordn1)




