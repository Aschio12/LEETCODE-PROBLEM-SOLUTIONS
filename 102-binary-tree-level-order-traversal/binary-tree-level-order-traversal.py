# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans,q=[[root.val]],deque([root])

        while q:
            current=[]
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    current.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    current.append(node.right.val)
                    q.append(node.right)
            if current:
                ans.append(current)
        return ans
        