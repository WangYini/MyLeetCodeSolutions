class Solution:
    def maxArea(self, height) -> int:
        '''solution 1'''
        #n = len(height)#9
        #max_area = 0
        #for delta_i in range(n - 1, 0, -1):#[8,7...1]
        #    left_edges = height[:n-delta_i]
        #    right_edges = height[delta_i:]
        #
        #    min_edges = [min(left_edges[i], right_edges[i]) for i in range(len(left_edges))]
        #    max_min_edge = max(min_edges)
        #    area = max_min_edge * delta_i
        #    if area > max_area:
        #        max_area = area

        '''solution2'''
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)

            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return max_area
            
a = Solution()
max = a.maxArea([1,8,6,2,5,4,8,3,7])
print(max)

