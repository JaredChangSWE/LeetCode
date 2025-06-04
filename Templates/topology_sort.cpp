#include <vector>
#include <queue>
#include <unordered_map>

std::unordered_map<int, int> find_indegree(const std::unordered_map<int, std::vector<int>>& graph) {
    std::unordered_map<int, int> indegree;
    for (const auto& kv : graph) {
        indegree[kv.first] = 0;
    }
    for (const auto& kv : graph) {
        for (int neighbor : kv.second) {
            indegree[neighbor]++;
        }
    }
    return indegree;
}

std::vector<int> topo_sort(const std::unordered_map<int, std::vector<int>>& graph) {
    std::vector<int> res;
    std::queue<int> q;
    auto indegree = find_indegree(graph);
    for (const auto& kv : indegree) {
        if (kv.second == 0) {
            q.push(kv.first);
        }
    }
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        res.push_back(node);
        for (int neighbor : graph.at(node)) {
            if (--indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    return res.size() == graph.size() ? res : std::vector<int>();
}
