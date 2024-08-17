# 1937. Maximum Number of Points with Cost

## Problem Statement

You are given an `m x n` integer matrix `points` (0-indexed). Starting with 0 points, your goal is to maximize the number of points you can gain from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates `(r, c)` will add `points[r][c]` to your score.

However, there is a cost associated with picking cells that are far apart in adjacent rows. Specifically, for every two adjacent rows `r` and `r + 1` (where `0 <= r < m - 1`), picking cells at coordinates `(r, c1)` and `(r + 1, c2)` will subtract `abs(c1 - c2)` from your score.

Return the maximum number of points you can achieve.

The function `abs(x)` is defined as:
- `x` for `x >= 0`.
- `-x` for `x < 0`.

## Examples

### Example 1

**Input:** 
```
points = [[1,2,3],[1,5,1],[3,1,1]]
```

**Output:** 
```
9
```

**Explanation:** 
The optimal cells to pick are at coordinates `(0, 2)`, `(1, 1)`, and `(2, 0)`. The score is calculated as follows:
- Points: `3 + 5 + 3 = 11`
- Cost: `abs(2 - 1) + abs(1 - 0) = 2`
- Final Score: `11 - 2 = 9`

### Example 2

**Input:** 
```
points = [[1,5],[2,3],[4,2]]
```

**Output:** 
```
11
```

**Explanation:** 
The optimal cells to pick are at coordinates `(0, 1)`, `(1, 1)`, and `(2, 0)`. The score is calculated as follows:
- Points: `5 + 3 + 4 = 12`
- Cost: `abs(1 - 1) + abs(1 - 0) = 1`
- Final Score: `12 - 1 = 11`

## Constraints

- `m == points.length`
- `n == points[r].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `0 <= points[r][c] <= 10^5`
