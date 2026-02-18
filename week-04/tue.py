#Practical Exercises with Fenwick Trees -Binary Indexed  
#Trees: Problem: Rainfall Measurement Using Fenwick Tree 

# Fenwick Tree (Binary Indexed Tree) Implementation
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    # Add value at index i
    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    # Prefix sum query from Day 1 to Day i
    def query(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total


# ----------------------------
# Rainfall Example Test Case
# ----------------------------

days = 6
rainfall = [5, 12, 7, 10, 6, 8]

# Build Fenwick Tree
ft = FenwickTree(days)

for i in range(days):
    ft.update(i + 1, rainfall[i])

print("Total rainfall till Day 4 =", ft.query(4), "mm")

# Update Day 3 rainfall from 7 → 9
old_value = rainfall[2]
new_value = 9
delta = new_value - old_value

rainfall[2] = new_value
ft.update(3, delta)

print("After update, total rainfall till Day 4 =", ft.query(4), "mm")

#✅ Output
Total rainfall till Day 4 = 34 mm
After update, total rainfall till Day 4 = 36 mm






#Problem: Online Course Watch-Time Analysis Using Fenwick Tree 
# Fenwick Tree (Binary Indexed Tree)
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    # Point update
    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    # Prefix sum query
    def query(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total


# ----------------------------
# Watch-Time Example Test Case
# ----------------------------

days = 5
watch_time = [30, 40, 20, 50, 10]

# Build Fenwick Tree
ft = FenwickTree(days)

for i in range(days):
    ft.update(i + 1, watch_time[i])

print("Total watch time till Day 4 =", ft.query(4))

# Update Day 2 watch time from 40 → 55
old_value = watch_time[1]
new_value = 55
delta = new_value - old_value

watch_time[1] = new_value
ft.update(2, delta)

print("After update, total watch time till Day 4 =", ft.query(4))

#✅ Output
Total watch time till Day 4 = 140
After update, total watch time till Day 4 = 155
