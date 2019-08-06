class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s
        group_len = numRows + numRows - 2
        result = ""
        for i in range(numRows):
            row = s[i::group_len]
            if i != 0 and i != numRows -1:
                between = s[group_len-i::group_len]
                si = ""
                if len(between)<len(row):
                    for j, a in enumerate(between):
                        si += row[j] + a
                    si += row[-1]
                elif len(between) == len(row):
                    for j, a in enumerate(between):
                        si += row[j] + a
            else:
                si = row
            result += si
        return result
a = Solution()
a.convert("LEETCODEISHIRING", 3)

