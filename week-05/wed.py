# Efficient Event Scheduling Using Red-Black Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"   # new nodes are inserted as RED
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NULL = Node(None)
        self.NULL.color = "BLACK"
        self.root = self.NULL

    # Left Rotate
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
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

    # Right Rotate
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
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

    # Insert
    def insert(self, key):
        node = Node(key)
        node.left = self.NULL
        node.right = self.NULL
        parent = None
        current = self.root

        while current != self.NULL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        node.color = "RED"
        self.fix_insert(node)

    # Fix Insert
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

    # Search
    def search(self, key):
        current = self.root
        while current != self.NULL:
            if key == current.data:
                return True
            elif key < current.data:
                current = current.left
            else:
                current = current.right
        return False

    # Transplant helper for delete
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Minimum node
    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    # Delete
    def delete(self, key):
        z = self.root
        while z != self.NULL:
            if z.data == key:
                break
            elif key < z.data:
                z = z.left
            else:
                z = z.right
        if z == self.NULL:
            return  # not found

        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "BLACK":
            self.fix_delete(x)

    # Fix Delete
    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == "BLACK" and s.right.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.right.color == "BLACK":
                        s.left.color = "BLACK"
                        s.color = "RED"
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.left.color == "BLACK" and s.right.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.left.color == "BLACK":
                        s.right.color = "BLACK"
                        s.color = "RED"
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"


# ----------------------------
# Example Test Case 1
# ----------------------------
tree = RedBlackTree()
events = [20, 15, 25, 10, 18, 30]

# Insert events
for e in events:
    tree.insert(e)

# Search(18)
print("FOUND" if tree.search(18) else "NOTFOUND")

# Delete(15)
tree.delete(15)

# Search(15)
print("FOUND" if tree.search(15) else "NOTFOUND")

## Real-Time Minimum and Maximum Query Using Segment Tree

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        # Each node stores (min, max)
        self.tree = [(float('inf'), float('-inf'))] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    # Build the segment tree
    def build(self, node, l, r):
        if l == r:
            self.tree[node] = (self.arr[l], self.arr[l])
        else:
            mid = (l + r) // 2
            self.build(node * 2, l, mid)
            self.build(node * 2 + 1, mid + 1, r)
            left = self.tree[node * 2]
            right = self.tree[node * 2 + 1]
            self.tree[node] = (min(left[0], right[0]), max(left[1], right[1]))

    # Range query
    def query(self, node, l, r, ql, qr):
        if qr < l or ql > r:
            return (float('inf'), float('-inf'))
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        left = self.query(node * 2, l, mid, ql, qr)
        right = self.query(node * 2 + 1, mid + 1, r, ql, qr)
        return (min(left[0], right[0]), max(left[1], right[1]))

    # Update a value
    def update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = (val, val)
            self.arr[idx] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(node * 2, l, mid, idx, val)
            else:
                self.update(node * 2 + 1, mid + 1, r, idx, val)
            left = self.tree[node * 2]
            right = self.tree[node * 2 + 1]
            self.tree[node] = (min(left[0], right[0]), max(left[1], right[1]))

    # Public methods
    def range_min(self, ql, qr):
        return self.query(1, 0, self.n - 1, ql, qr)[0]

    def range_max(self, ql, qr):
        return self.query(1, 0, self.n - 1, ql, qr)[1]

    def update_value(self, idx, val):
        self.update(1, 0, self.n - 1, idx, val)


# ----------------------------
# Example Test Case 1
# ----------------------------
n = 8
readings = [32, 28, 30, 35, 29, 31, 34, 33]

seg_tree = SegmentTree(readings)

# RangeMin(2,6) -> indices are 0-based
print(seg_tree.range_min(2, 6))   # 29

# RangeMax(1,5)
print(seg_tree.range_max(1, 5))   # 35

# Update(3,27) -> index 3 becomes 27
seg_tree.update_value(3, 27)

# RangeMin(2,6)
print(seg_tree.range_min(2, 6))   # 27
