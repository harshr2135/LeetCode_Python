class Solution:
    def trap(self, height: List[int]) -> int:
        prevMax = height[0]
        leftMax = [0] * len(height)
        for idx in range(len(height)):
            prevMax = max(prevMax, height[idx])
            leftMax[idx] = prevMax

        frontMax = height[len(height)-1]
        rightMax = [0] * len(height)
        for idx in range(len(height)-1, -1, -1):
            frontMax = max(frontMax, height[idx])
            rightMax[idx] = frontMax

        water = 0
        for idx in range(len(height)):
            water += max(0, min(leftMax[idx], rightMax[idx])-height[idx])

        return water
