#include <vector>
#include <queue>
#include <functional>

struct Node {
    std::vector<Node*> children;
};

Node* bfs(Node* root, const std::function<bool(Node*)>& is_goal) {
    if (root == nullptr) return nullptr;
    std::queue<Node*> q;
    q.push(root);
    while (!q.empty()) {
        Node* node = q.front();
        q.pop();
        if (is_goal(node)) {
            return node; // FOUND
        }
        for (Node* child : node->children) {
            if (child != nullptr) {
                q.push(child);
            }
        }
    }
    return nullptr; // NOT_FOUND
}
