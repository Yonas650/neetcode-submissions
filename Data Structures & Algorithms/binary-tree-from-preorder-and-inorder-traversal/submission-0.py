# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self,root, val):
        if not root:
            return TreeNode(val)
        if val< root.val:
            root.left=self.insert(root.left,val)
        elif val> root.val:
            root.right=self.insert(root.right,val)
        
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root