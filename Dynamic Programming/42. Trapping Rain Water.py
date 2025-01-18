" Done before "
" What you do is you have 2 pointers at the sides of the array "
" Then move inwards by moving the smaller pointer and take the difference between that pointer and the tallest on it's side "

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        res = 0
        
        while l < r:
            if lMax >= rMax:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
            else:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
        return res
            