class Solution(object):
    def kthCharacter(self, k, operations):
        # We track only lengths at each step (without building full string)
        lengths = [1]  # initial length of word = "a"
        
        for op in operations:
            prev_len = lengths[-1]
            if op == 0:
                lengths.append(prev_len * 2)
            else:
                lengths.append(prev_len * 2)  # since it's original + transformed

        ch = 'a'  # initial character

        for i in range(len(operations) - 1, -1, -1):
            op = operations[i]
            half = lengths[i]

            if k > half:
                # k refers to a character in the second half
                k -= half
                if op == 1:
                    # Move character forward in alphabet
                    ch = chr(((ord(ch) - ord('a') + 1) % 26) + ord('a'))
            else:
                # k is still in the first half, character remains same
                continue

        return ch

        