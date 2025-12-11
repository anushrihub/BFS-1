# https://leetcode.com/problems/binary-tree-level-order-traversal/

# approach 1 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        # to strore the result
        result = []
        # queue, at the start it contains only root node and then we are increasing the size
        q = [root]
        # as long as there are elements in the queue, perform the operation
        while q:
            # this defines the number of nodes currently in the queue
            size = len(q)
            # a temporary list 
            temp = []
            for i in range(size):
                # remove the first element from the queue
                curr = q.pop(0)
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(temp)
        return result
# approach 2   
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
        self.helper(root.right, level + 1)