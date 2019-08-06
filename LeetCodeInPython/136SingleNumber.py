class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        repeat = [nums[0]]
        for i in nums[1:]:
            if i in repeat:
                repeat.remove(i)
            else:
                repeat.append(i)
        return repeat[0]
