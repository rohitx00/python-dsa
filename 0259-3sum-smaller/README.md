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

