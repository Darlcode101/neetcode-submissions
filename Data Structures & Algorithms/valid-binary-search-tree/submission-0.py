# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):

            if node is None:
                return True

            # check if node.val is inside the valid range
            if node.val >= maximum or node.val<=minimum:
                return False
            

            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)

        return valid(root, float("-inf"), float("inf"))
    