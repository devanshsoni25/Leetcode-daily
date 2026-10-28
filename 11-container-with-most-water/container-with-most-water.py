class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        max_area = 0

        while i<j:
            width = j - i
            height_c = min(height[i],height[j])
        
            area = height_c*width

            max_area = max(area,max_area)
            if height[i]<height[j]:
                i+=1

            else:
                j-=1
        return max_area