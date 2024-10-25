class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return

        root = TrieNode()
        for l in folder:
            curr = root
            for c in l.split("/"):
                if c not in curr.child:
                    curr.child[c] = TrieNode()
                curr = curr.child[c] 
            curr.is_word = True

        result = []
        for l in folder:
            if self.search(root, l):
                result.append(l)
        return result

    def search(self, root, l):
        curr = root
        array = l.split("/")
        for i in range(len(array)):
            curr = curr.child[array[i]]
            if curr.is_word and i != len(array)-1:
                return False
        return True
        