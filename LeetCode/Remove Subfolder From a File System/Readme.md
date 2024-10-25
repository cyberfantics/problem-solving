# Problem: Remove Sub-Folders from the Filesystem

Given a list of folder paths, return the folders after removing all sub-folders from those folders. You may return the answer in any order.

If `folder[i]` is located within another `folder[j]`, it is called a sub-folder of `folder[j]`. A sub-folder of `folder[j]` must start with `folder[j]`, followed by a `/`. For example, `/a/b` is a sub-folder of `/a`, but `/b` is not a sub-folder of `/a/b/c`.

The format of a path is one or more concatenated strings of the form: `'/'` followed by one or more lowercase English letters.

**Examples of valid paths**: `/leetcode` and `/leetcode/problems`

**Examples of invalid paths**: an empty string and `/`

## Example 1:

**Input**:
```folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]```

**Output**:
```["/a", "/c/d", "/c/f"]```


**Explanation**: 
Folders `/a/b` is a sub-folder of `/a` and `/c/d/e` is inside the folder `/c/d` in our filesystem.

## Example 2:

**Input**:
```folder = ["/a", "/a/b/c", "/a/b/d"]```

**Output**:
```["/a"]```

## Constraints:

- `1 <= folder.length <= 4 * 10^4`
- `2 <= folder[i].length <= 100`
- `folder[i]` contains only lowercase letters and `'/'`.
- `folder[i]` always starts with the character `'/'`.
- Each folder name is unique.
