import numpy as np
class Solution(object):
    def productExceptSelf(self, nums):
        p = 1
        out = []
        
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
            
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out