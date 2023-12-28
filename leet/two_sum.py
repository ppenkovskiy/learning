class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

res = Solution()
nums = [2,7,11,15]
target = 9
print(res.twoSum(nums, target))

nums = [3,2,4]
target = 6
print(res.twoSum(nums, target))

nums = [3,3]
target = 6
print(res.twoSum(nums, target))