# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Time complexity -O(n) Space Complexity- O(h)  
class Solution:
    def levelOrder(self, root):
        # initialise the result
        self.result = []
        # call the recursive helper function, initially the level is 0 for the root node
        self.helper(root, 0)
        return self.result

    def helper(self, root, level):
        # handdling the edge case ending the recusrion when node is Null
        if root is None:
            # it returns nothing
            return
        # checking the length of the result which has the number of nodes with the level 
        if len(self.result) == level:
            # add the new empty list
            self.result.append([])
        # once the empty list is added, add the node value into that list
        self.result[level].append(root.val)
        # recursivly calling the function to get the left node values with increasing the existing level
        self.helper(root.left, level + 1)
        # recursivly calling the function to get the right node values with increasing the existing level
        self.helper(root.right, level + 1)