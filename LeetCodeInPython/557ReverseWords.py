class Solution:
    def reverseWords(self, s: str) -> str:
        #listOfWords = s.split(" ")
        #reversedListOfWords = [word[::-1] for word in listOfWords]
        #return " ".join(reversedListOfWords)
        reversed_s = s[::-1]
        listOfWords = reversed_s.split(" ")
        return " ".join(listOfWords[::-1])
a = Solution()
b = a.reverseWords("let us do leetcode exercises")
print(b)
