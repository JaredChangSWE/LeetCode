class UnionFind:

    def __init__(self, size: int):
        self.root = list(range(size))
        self.rank = [0] * size

    def find(self, u: int) -> int:
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]

    def union(self, u: int, v: int) -> None:
        root_u, root_v = self.find(u), self.find(v)

        if root_u == root_v:
            return False # cycle detected

        if self.rank[root_u] > self.rank[root_v]:
            self.root[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.root[root_u] = root_v
        else:
            self.root[root_u] = root_v
            self.rank[root_v] += 1

        return True