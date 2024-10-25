class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders alphabetically
        folder.sort()
        result = []

        # Iterate over sorted folders
        for f in folder:
            # If the current folder is not a subfolder of the last added folder, add it to result
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)

        return result