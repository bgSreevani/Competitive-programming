#Segment Tree for Range Minimum Query (RMQ)

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Build Segment Tree
def build(seg, arr, idx, low, high):
    if low == high:
        seg[idx] = arr[low]
        return

    mid = (low + high) // 2
    build(seg, arr, 2 * idx + 1, low, mid)
    build(seg, arr, 2 * idx + 2, mid + 1, high)

    seg[idx] = min(seg[2 * idx + 1], seg[2 * idx + 2])


# Query Segment Tree
def query(seg, idx, low, high, l, r):
    # No overlap
    if r < low or high < l:
        return float("inf")

    # Complete overlap
    if l <= low and high <= r:
        return seg[idx]

    # Partial overlap
    mid = (low + high) // 2
    left_min = query(seg, 2 * idx + 1, low, mid, l, r)
    right_min = query(seg, 2 * idx + 2, mid + 1, high, l, r)

    return min(left_min, right_min)


# Driver Code
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # Segment tree size (4*N is safe)
    seg = [0] * (4 * N)

    # Build tree
    build(seg, arr, 0, 0, N - 1)

    Q = int(input())

    for _ in range(Q):
        L, R = map(int, input().split())
        print(query(seg, 0, 0, N - 1, L, R))


#✅ Sample Input
1
6
2 -1 4 0 3 -5
3
0 3
2 5
1 4

#✅ Sample Output
-1
-5
-1





# Segment Tree with Point Updates
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Build Segment Tree
def build(seg, arr, idx, low, high):
    if low == high:
        seg[idx] = arr[low]
        return

    mid = (low + high) // 2
    build(seg, arr, 2 * idx + 1, low, mid)
    build(seg, arr, 2 * idx + 2, mid + 1, high)

    seg[idx] = seg[2 * idx + 1] + seg[2 * idx + 2]


# Point Update
def update(seg, idx, low, high, pos, val):
    if low == high:
        seg[idx] = val
        return

    mid = (low + high) // 2
    if pos <= mid:
        update(seg, 2 * idx + 1, low, mid, pos, val)
    else:
        update(seg, 2 * idx + 2, mid + 1, high, pos, val)

    seg[idx] = seg[2 * idx + 1] + seg[2 * idx + 2]


# Range Sum Query
def query(seg, idx, low, high, l, r):
    # No overlap
    if r < low or high < l:
        return 0

    # Complete overlap
    if l <= low and high <= r:
        return seg[idx]

    # Partial overlap
    mid = (low + high) // 2
    left_sum = query(seg, 2 * idx + 1, low, mid, l, r)
    right_sum = query(seg, 2 * idx + 2, mid + 1, high, l, r)

    return left_sum + right_sum


# Driver Code
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    seg = [0] * (4 * N)

    # Build tree
    build(seg, arr, 0, 0, N - 1)

    Q = int(input())

    for _ in range(Q):
        q = list(map(int, input().split()))

        if q[0] == 1:
            # Update query: 1 i x
            i, x = q[1], q[2]
            update(seg, 0, 0, N - 1, i, x)

        elif q[0] == 2:
            # Sum query: 2 L R
            L, R = q[1], q[2]
            print(query(seg, 0, 0, N - 1, L, R))
#✅ Sample Input
1
5
1 3 5 7 9
4
2 1 3
1 2 10
2 1 3
2 0 4

#✅ Sample Output
15
20
30
