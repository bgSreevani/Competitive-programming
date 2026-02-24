##Efficient Event Scheduling Using Red-Black Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.color = "RED"  # New nodes are always RED
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    # ------------------------
    # Left Rotate
    # ------------------------
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # ------------------------
    # Right Rotate
    # ------------------------
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # ------------------------
    # Insert
    # ------------------------
    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = "RED"
        self.fix_insert(node)

    # Fix violations after insert
    def fix_insert(self, k):
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)

        self.root.color = "BLACK"

    # ------------------------
    # Search
    # ------------------------
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # ------------------------
    # Delete
    # ------------------------
    def delete(self, key):
        node = self.search(key)
        if node == self.NIL:
            return

        self._delete_node(node)

    def _delete_node(self, z):
        if z.left == self.NIL:
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            z.key = y.key
            self._delete_node(y)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node


# -------------------------
# Example Test Case
# -------------------------

rbt = RedBlackTree()

# Insert event times
events = [20, 15, 25, 10, 18, 30]
for event in events:
    rbt.insert(event)

# Search(18)
if rbt.search(18) != rbt.NIL:
    print("FOUND")
else:
    print("NOTFOUND")

# Delete(15)
rbt.delete(15)

# Search(15)
if rbt.search(15) != rbt.NIL:
    print("FOUND")
else:
    print("NOTFOUND")


##Real-Time Minimum and Maximum Query Using Segment Tree

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.min_tree = [0] * (4 * self.n)
        self.max_tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    # -------------------------
    # Build Segment Tree
    # -------------------------
    def build(self, node, start, end):
        if start == end:
            self.min_tree[node] = self.arr[start]
            self.max_tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)

            self.min_tree[node] = min(
                self.min_tree[2 * node + 1],
                self.min_tree[2 * node + 2]
            )
            self.max_tree[node] = max(
                self.max_tree[2 * node + 1],
                self.max_tree[2 * node + 2]
            )

    # -------------------------
    # Range Minimum Query
    # -------------------------
    def range_min(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.min_tree[node]

        mid = (start + end) // 2
        left = self.range_min(2 * node + 1, start, mid, l, r)
        right = self.range_min(2 * node + 2, mid + 1, end, l, r)
        return min(left, right)

    # -------------------------
    # Range Maximum Query
    # -------------------------
    def range_max(self, node, start, end, l, r):
        if r < start or end < l:
            return float('-inf')
        if l <= start and end <= r:
            return self.max_tree[node]

        mid = (start + end) // 2
        left = self.range_max(2 * node + 1, start, mid, l, r)
        right = self.range_max(2 * node + 2, mid + 1, end, l, r)
        return max(left, right)

    # -------------------------
    # Update Value
    # -------------------------
    def update(self, node, start, end, idx, value):
        if start == end:
            self.arr[idx] = value
            self.min_tree[node] = value
            self.max_tree[node] = value
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, value)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, value)

            self.min_tree[node] = min(
                self.min_tree[2 * node + 1],
                self.min_tree[2 * node + 2]
            )
            self.max_tree[node] = max(
                self.max_tree[2 * node + 1],
                self.max_tree[2 * node + 2]
            )


# -------------------------
# Example Test Case
# -------------------------

temperatures = [32, 28, 30, 35, 29, 31, 34, 33]
st = SegmentTree(temperatures)

# RangeMin(2,6) -> 1-based indexing given in question
print(st.range_min(0, 0, 7, 1, 5))  # Converted to 0-based

# RangeMax(1,5)
print(st.range_max(0, 0, 7, 0, 4))

# Update(3,27)
st.update(0, 0, 7, 2, 27)  # index 3 -> 2 in 0-based

# RangeMin(2,6) after update
print(st.range_min(0, 0, 7, 1, 5))
