# integer array nums where nums[i] represents the amount of money the ith house has

# cannot rob two adjacent houses

# maximum amount of money you can rob without alerting.

# nums = [1,1,3,3]

# Decisions

# - rob ith house
#     - skip i+1 = rob i+2
# - skip ith house
#     - rob i+1 th or skip i+1 th = rob i+2

# if rob
#   goto i+2, get i money
# else
#   max (goto i+1 or goto i+2, get i moeny)

# => max (goto i+1 or goto i+2, get i moeny)

# => dp[i] = max(dp[i+1], dp[i+2] + nums[i])

#############################

# V1 for Memoization
# class Solution:
#     def rob(self, nums: List[int]) -> int:

#         dp = [None] * len(nums)

#         def decideToRob(current_house_index: int) -> int:
            
#             if current_house_index >= len(nums):
#                 return 0
            
#             if dp[current_house_index]:
#                 return dp[current_house_index]

#             dp[current_house_index] = max(decideToRob(current_house_index + 1), 
#                        decideToRob(current_house_index + 2) + nums[current_house_index])

#             return dp[current_house_index]

#         return decideToRob(0)

#############################

# => dp[i] = max(dp[i+1], dp[i+2] + nums[i])
# calculate from dp[len(nums) - 1]
# base case
# dp[len(nums) - 1] = nums[-1] due to max(dp[i+1], dp[i+2] + nums[i])
# dp[len(nums) - 2] = max(nums[-1], nums[-2]) due to max(dp[i+1], dp[i+2] + nums[i])


# V2 for Tabulation
# class Solution:
#     def rob(self, nums: List[int]) -> int:

#         if len(nums) == 1:
#             return nums[0]

#         dp = [None] * len(nums)

#         dp[-1] = nums[-1]
#         dp[-2] = max(nums[-2], nums[-1])

#         for i in range(len(nums)-3, -1, -1):
#             dp[i] = max(dp[i+1], dp[i+2] + nums[i])

#         return dp[0]



#############################

# Actions

# - rob ith house
#     - skip i+1 = rob i+2
# - skip ith house
#     - rob i+1 th or skip i+1 th = rob i+2

# what is the max profit after currect action?
#
# - rob ith house
#     - ith money + max money if I rob i-2 house
# - skip ith house
#     - max money if I rob i-1 house
#

# => max (i-1, i-2 + money[i])

# => dp[i] = max(dp[i-1], dp[i-2] + nums[i])
# base case: 0 if i < 0

# V3 for Tabulation in order
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = [None] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]