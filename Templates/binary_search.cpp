#include <vector>
#include <cstddef>

class Solution {
public:
    int search(const std::vector<int>& nums, int target) {
        return bisect_exactly(nums, target);
    }

    int bisect_left(const std::vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if (left >= 0 && left < (int)nums.size() && nums[left] == target) {
            return left;
        }
        return -1;
    }

    int bisect_right(const std::vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if (right - 1 >= 0 && right - 1 < (int)nums.size() && nums[right - 1] == target) {
            return right - 1;
        }
        return -1;
    }

    int bisect_exactly(const std::vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
};
