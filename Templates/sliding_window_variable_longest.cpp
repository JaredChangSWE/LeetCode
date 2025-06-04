#include <vector>
#include <algorithm>

// Placeholder for user-defined helpers
bool invalid(const std::vector<int>& window);
int optimal(const std::vector<int>& window);

int sliding_window_flexible_longest(const std::vector<int>& input) {
    int answer = 0;
    std::vector<int> window;
    int left = 0;
    for (int right = 0; right < (int)input.size(); ++right) {
        window.push_back(input[right]);
        while (invalid(window)) {
            int left_elem = input[left];
            auto it = std::find(window.begin(), window.end(), left_elem);
            if (it != window.end()) {
                window.erase(it);
            }
            ++left;
        }
        answer = std::max(answer, optimal(window));
    }
    return answer;
}
