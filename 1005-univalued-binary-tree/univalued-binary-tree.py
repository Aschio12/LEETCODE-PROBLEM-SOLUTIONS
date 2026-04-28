class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        comp=root.val
        q=deque([root])
        

        def bfs(node):
            if node.val!=comp:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)                    

            
            while q:
                node=q.popleft()
                ret=bfs(node)
                if ret==False:
                    return ret
            return True

        return bfs(root)
                