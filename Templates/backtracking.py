class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(start: int, current_nums: list[int]) -> None:
            nonlocal answer

            answer.append(current_nums.copy())

            for i in range(start, len(nums)):
                current_nums.append(nums[i])
                dfs(i + 1, current_nums)
                current_nums.pop()

        dfs(0, [])

        return answer