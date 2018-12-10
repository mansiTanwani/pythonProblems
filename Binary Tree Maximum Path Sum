# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        max_sum = -10000000
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxPathSum(self,root):
            
            def maxsum(self, root, max_sum):
                if root == None:
                    return 0
                left_max = 0
                right_max = 0
                sum_node = root.val
                if root.left:
                    left_max = maxsum(self, root.left, max_sum)
                    
                    if left_max > 0:
                        sum_node += left_max
                        
                if root.right:
                    right_max = maxsum(self, root.right, max_sum)
                    if right_max > 0:
                        sum_node += right_max
                if sum_node > self.max_sum:
                    self.max_sum = sum_node
                    
                return max(root.val, max(root.val + left_max, root.val + right_max))
                
            max_sum = -10000000
            if root == None:
                return 0
            maxsum(self, root, max_sum)
            return self.max_sum
