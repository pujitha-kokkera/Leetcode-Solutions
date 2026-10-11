class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                s=nums[i]+nums[j]
                if(s==target):
                    return [i,j]
nums=[2,7,11,15]
target=9
solution=Solution()
print(solution.twoSum(nums, target))
