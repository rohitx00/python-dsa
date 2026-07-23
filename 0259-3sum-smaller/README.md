# 259. 3Sum Smaller

## 🟢 Difficulty
Medium *(LeetCode Premium)*

---

## Problem Statement

Given an integer array `nums` of length `n` and an integer `target`, find the number of index triplets `(i, j, k)` such that:

- `0 <= i < j < k < n`
- `nums[i] + nums[j] + nums[k] < target`

Return the total number of such triplets.

---

## Example 1

```text
Input: nums = [-2,0,1,3], target = 2
Output: 2

Explanation:
The valid triplets are:
(-2,0,1) -> sum = -1
(-2,0,3) -> sum = 1
```

---

## Example 2

```text
Input: nums = [-1,2,1,-4], target = 2
Output: 3

Explanation:
After sorting: [-4,-1,1,2]

The valid triplets are:
(-4,-1,1) -> -4
(-4,-1,2) -> -3
(-4,1,2)  -> -1
```

---

## Constraints

- `3 <= nums.length <= 3500`
- `-100 <= nums[i] <= 100`
- `-100 <= target <= 100`

---

## Follow Up

Can you solve the problem in **O(n²)** time instead of checking every possible triplet?

---

## Approach

Since the array is not necessarily sorted, first sort it.

Then:

1. Fix one element at index `i`.
2. Use two pointers:
   - `left = i + 1`
   - `right = n - 1`
3. If the current sum is smaller than the target:
   - Every triplet between `left` and `right` is also valid because the array is sorted.
   - Add `(right - left)` to the answer.
   - Move `left` forward.
4. Otherwise, move `right` backward.

---

## Time Complexity

- **Time:** `O(n²)`
- **Space:** `O(1)` *(excluding sorting)*

---

## Tags

- Array
- Two Pointers
- Sorting
- Binary Search