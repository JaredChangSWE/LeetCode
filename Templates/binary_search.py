class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bisect_exatly(nums, target)

    def bisect_left(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if left >= 0 and nums[left] == target:
            return left

        return -1

    def bisect_right(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if right <= len(nums) and nums[right - 1] == target:
            return right - 1

        return -1

    def bisect_exatly(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
