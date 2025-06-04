#include <vector>

class UnionFind {
public:
    explicit UnionFind(int size) : root(size), rank(size, 0) {
        for (int i = 0; i < size; ++i) {
            root[i] = i;
        }
    }

    int find(int u) {
        if (root[u] != u) {
            root[u] = find(root[u]);
        }
        return root[u];
    }

    bool union_set(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u == root_v) {
            return false; // cycle detected
        }
        if (rank[root_u] > rank[root_v]) {
            root[root_v] = root_u;
        } else if (rank[root_u] < rank[root_v]) {
            root[root_u] = root_v;
        } else {
            root[root_u] = root_v;
            rank[root_v] += 1;
        }
        return true;
    }

private:
    std::vector<int> root;
    std::vector<int> rank;
};
