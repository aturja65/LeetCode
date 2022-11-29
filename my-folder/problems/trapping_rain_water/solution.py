class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        ans = 0
        while left<right:
            if leftMax<rightMax:
                left+=1
                leftMax = max(leftMax,height[left])
                ans += leftMax-height[left]
            else:
                right-=1
                rightMax = max(rightMax,height[right])
                ans += rightMax-height[right]
        return ans