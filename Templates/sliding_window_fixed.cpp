#include <vector>
#include <algorithm>

// Placeholder for user-defined optimal check
bool optimal(const std::vector<int>& window);

bool checkInclusion(const std::vector<int>& input, int window_size) {
    int left = 0;
    std::vector<int> window;
    for (int right = 0; right < (int)input.size(); ++right) {
        int right_element = input[right];
        window.push_back(right_element);
        if (optimal(window)) {
            return true;
        }
        int left_element = input[left];
        auto it = std::find(window.begin(), window.end(), left_element);
        if (it != window.end()) {
            window.erase(it);
        }
        ++left;
    }
    return false;
}
