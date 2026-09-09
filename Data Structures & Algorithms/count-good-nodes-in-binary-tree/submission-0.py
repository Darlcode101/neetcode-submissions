# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        if root is None:
            return 0
        
        queue = [(root, root.val)]

        while queue:
            node, biggest = queue.pop(0)
            
            if node.val >= biggest:
                good += 1
            
            new_biggest = max(biggest, node.val)

            if node.left:
                queue.append((node.left, new_biggest))

            if node.right:
                queue.append((node.right, new_biggest))
            
        return good

        