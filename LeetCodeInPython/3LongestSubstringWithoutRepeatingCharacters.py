class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        max = 1

        if not s:
            return 0

        while i + j<=len(s):
            sub = s[i:i+j]

            if i+j == len(s):
                break

            next_char = s[i+j]

            if next_char not in sub:
                j += 1
            else:
                i += 1
                if j > max:
                    max = j
                j = 1
        if j > max:
            max = j
        return max

a = Solution()

print(a.lengthOfLongestSubstring("pwwkew"))

