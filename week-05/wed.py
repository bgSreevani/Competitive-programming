class DSU:
    def __init__(self, n):
        # Step 1: Initialize parent and rank
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    # Step 2: Find with Path Compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Step 3: Union by Rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    # Step 4: Check Connectivity
    def connected(self, x, y):
        return self.find(x) == self.find(y)


# -----------------------------
# Example Test Case 1
# -----------------------------

n = 8  # Number of intersections
dsu = DSU(n)

# Roads constructed
roads = [(1,2), (2,3), (4,5), (6,7), (5,6)]

for u, v in roads:
    dsu.union(u, v)

# Connectivity Queries
queries = [(1,3), (1,7), (4,7)]

for u, v in queries:
    if dsu.connected(u, v):
        print("YES")
    else:
        print("NO")
