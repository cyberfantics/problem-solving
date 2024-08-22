## The Minion Game

### Game Rules
- Both players are given the same string `s`.
- Stuart forms words starting with consonants.
- Kevin forms words starting with vowels.
- The game ends when all possible substrings have been formed.

### Scoring
- Each player gets +1 point for each occurrence of their substring in `s`.

### Example
**Input**: `BANANA`

- Kevin's vowel word: `ANA` occurs twice in `BANANA`. Kevin gets 2 points.

### Task
Determine the winner and their score.

### Input Format
A single line of input containing the string s.

### Output Format
Print the winner's name and score separated by a space, or Draw if there is no winner.

### Constraints
The string s will contain only uppercase letters (A-Z).

### Sample Input
```BANANA```

### Sample Output
```Stuart 12```

