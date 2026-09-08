# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        res= []
        queue = [root]

        while queue:
            level = []
            levelSize = len(queue)

            for i in range(levelSize):
                index = queue.pop(0)

                level.append(index.val)

                if index.left:
                    queue.append(index.left)

                if index.right:
                    queue.append(index.right)
                
                
                
            res.append(level)

        return res
                
                

        


            