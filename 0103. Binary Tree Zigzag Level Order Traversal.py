# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        order = True

        while queue:
            currLevel = []

            for _ in range(len(queue)):
                node = queue.popleft()
                currLevel.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            if order:
                res.append(currLevel)
        
            else:
                res.append(currLevel[::-1])
                
            order = not order
        return res