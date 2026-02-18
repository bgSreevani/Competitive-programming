# Count Subsets with Given Sum

from itertools import combinations
from collections import Counter

def count_subsets_with_sum(arr, S):
    n = len(arr)
    
    # Split array into two halves
    left = arr[:n // 2]
    right = arr[n // 2:]

    # Generate all subset sums of left half
    left_sums = []
    for r in range(len(left) + 1):
        for comb in combinations(left, r):
            left_sums.append(sum(comb))

    # Generate all subset sums of right half
    right_sums = []
    for r in range(len(right) + 1):
        for comb in combinations(right, r):
            right_sums.append(sum(comb))

    # Count occurrences of right sums
    right_counter = Counter(right_sums)

    # Count valid pairs
    count = 0
    for ls in left_sums:
        count += right_counter[S - ls]

    return count


# Driver Code
T = int(input())
for _ in range(T):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    print(count_subsets_with_sum(arr, S))


#Sample Input
1
4 5
1 2 3 4

#Sample Output
2





# Closest Subset Sum

from itertools import combinations
import bisect

def closest_subset_sum(arr, S):
    n = len(arr)

    # Split array into two halves
    left = arr[:n // 2]
    right = arr[n // 2:]

    # Generate all subset sums of left half
    left_sums = []
    for r in range(len(left) + 1):
        for comb in combinations(left, r):
            left_sums.append(sum(comb))

    # Generate all subset sums of right half
    right_sums = []
    for r in range(len(right) + 1):
        for comb in combinations(right, r):
            right_sums.append(sum(comb))

    # Sort right sums for binary search
    right_sums.sort()

    # Initialize minimum difference
    min_diff = float("inf")

    # For each sum in left, find best match in right
    for ls in left_sums:
        target = S - ls

        # Binary search in right_sums
        idx = bisect.bisect_left(right_sums, target)

        # Check closest values around idx
        if idx < len(right_sums):
            min_diff = min(min_diff, abs(ls + right_sums[idx] - S))
        if idx > 0:
            min_diff = min(min_diff, abs(ls + right_sums[idx - 1] - S))

    return min_diff


# Driver Code
T = int(input())
for _ in range(T):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    print(closest_subset_sum(arr, S))


#Sample Input
1
4 5
1 2 3 4

#✅ Sample Output
0
