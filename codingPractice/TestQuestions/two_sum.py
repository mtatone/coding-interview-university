# class Solution:
#     @staticmethod
#     def twoSum(nums, target):
#         if len(nums) == 2:
#             return [0, 1]
#         else:
#             # for i, num in enumerate(nums):
#             #     diff = float(target - num)
#             #     print("{}). {} - ({}) = {}".format(i, target, num, diff))
#             #     if diff in nums:
#             #         return [i, nums.index(diff)]
#             for i in range(len(nums)):
#                 num = nums.pop(0)
#                 diff = target - num
#                 if diff in nums:
#                     return [i, nums.index(diff) + 1 + i]


# Using a dictionary for faster operations

class Solution:
    @staticmethod
    def twoSum(nums, target):
        if len(nums) == 2:
            return [0, 1]
        else:
            diff_mem = {} # difference : index
            for i in range(len(nums)):
                if nums[i] in diff_mem:
                    return [diff_mem[nums[i]], i]
                diff = target - nums[i]
                diff_mem[diff] = i



sol = Solution.twoSum(nums=[2, 7, 11, 15], target=9)
# sol = Solution.twoSum(nums=[3, 2, 4], target=6)
print(sol)


