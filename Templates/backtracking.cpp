#include <vector>
#include <functional>

class Solution {
public:
    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        std::vector<std::vector<int>> answer;
        std::vector<int> current;
        std::function<void(int)> dfs = [&](int start) {
            answer.push_back(current);
            for (int i = start; i < (int)nums.size(); ++i) {
                current.push_back(nums[i]);
                dfs(i + 1);
                current.pop_back();
            }
        };
        dfs(0);
        return answer;
    }
};
