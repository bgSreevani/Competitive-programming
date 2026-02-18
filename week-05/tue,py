#Community Detection in a Social Networking Platform (DSU / Union-Find)

# Disjoint Set Union (Union-Find) Implementation
class DSU:
    def __init__(self, n):
        # Parent array: each node is its own parent initially
        self.parent = list(range(n))
        # Rank array for union by rank optimization
        self.rank = [0] * n

    # Find with Path Compression
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    # Union by Rank
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU == rootV:
            return

        # Attach smaller rank tree under bigger rank tree
        if self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV
        elif self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1

    # Check if two users are connected
    def connected(self, u, v):
        return self.find(u) == self.find(v)


# ----------------------------
# Example Test Case 1
# ----------------------------

# Number of users
n = 7

# Friendships
friendships = [(0, 1), (1, 3), (2, 4), (5, 6), (3, 4)]

# Queries
queries = [(0, 4), (2, 6), (5, 6)]

# Initialize DSU
dsu = DSU(n)

# Process friendships (Union operations)
for u, v in friendships:
    dsu.union(u, v)

# Answer queries
for u, v in queries:
    if dsu.connected(u, v):
        print("YES")
    else:
        print("NO")

#✅ Sample Input (Given)
Users = 7
Friendships = 5
(0,1)
(1,3)
(2,4)
(5,6)
(3,4)

Queries:
(0,4)
(2,6)
(5,6)

#✅ Output
YES
NO
YES



#ity Road Connectivity Management (DSU / Union-Find)

# Disjoint Set Union (Union-Find)
class DSU:
    def __init__(self, n):
        # Each intersection is its own parent initially
        self.parent = list(range(n))
        self.rank = [0] * n

    # Find with Path Compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by Rank
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1

    # Connectivity Check
    def connected(self, a, b):
        return self.find(a) == self.find(b)


# ----------------------------
# Example Test Case 1
# ----------------------------

# Number of intersections
n = 8

# Roads constructed
roads = [(1, 2), (2, 3), (4, 5), (6, 7), (5, 6)]

# Connectivity queries
queries = [(1, 3), (1, 7), (4, 7)]

# Initialize DSU
dsu = DSU(n)

# Process roads (Union operations)
for u, v in roads:
    dsu.union(u, v)

# Answer queries
for u, v in queries:
    if dsu.connected(u, v):
        print("YES")
    else:
        print("NO")

#✅ Sample Input (Given)
Intersections = 8
Roads = 5
(1,2)
(2,3)
(4,5)
(6,7)
(5,6)

Queries:
(1,3)
(1,7)
(4,7)


#✅ Output
YES
NO
YES
